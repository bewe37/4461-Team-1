import random
from mesa import Model
from mesa.datacollection import DataCollector
from mesa.space import SingleGrid
from agents import SocialMediaUser

# Custom RandomActivation Scheduler because we can't import mesa.time
class RandomActivation:
    def __init__(self, model):
        self.model = model
        self.agents = []
    
    def add(self, agent):
        self.agents.append(agent)
    
    def step(self):
        random.shuffle(self.agents)
        for agent in self.agents:
            agent.step()

class Schelling(Model):

    human_type = 0
    bot_type = 1

    def __init__(
        self,
        height: int = 20,
        width: int = 20,
        density: float = 0.8,
        bot_ratio: float = 0.1,
        bot_influence: float = 0.5,
        seed=None,
        homophily: float = 0.5,
    ):
        """
        :param height: Grid height
        :param width: Grid width
        :param density: Probability of a cell being initially occupied
        :param bot_ratio: Probability that an agent will be a bot
        :param bot_influence: Probability that a bot will change a humans belief
        :param seed: Optional random seed
        :param homophily: How happy an agent is
        """
        super().__init__(seed=seed)

        self.height = height
        self.width = width
        self.density = density
        self.bot_ratio = bot_ratio
        self.bot_influence = bot_influence
        self.total_clusters = 0
        self.happy = 0
        self.homophily = homophily

        # Initialize a SingleGrid (toroidal means wrapping edges)
        self.grid = SingleGrid(width, height, torus=True)

        # Initialize our custom random activation scheduler
        self.schedule = RandomActivation(self)

        # Place agents and add them to the scheduler
        for _, pos in self.grid.coord_iter():
            if self.random.random() < self.density:
                agent_type = self.bot_type if self.random.random() < self.bot_ratio else self.human_type

                # Prevents bots from spawning next to one another
                if agent_type == self.bot_type:
                    neighbors = self.grid.get_neighborhood(pos, moore=True, include_center=False)
                    neighbors_agents = self.grid.get_cell_list_contents(neighbors)

                    if any(neighbor_agent.type == self.bot_type for neighbor_agent in neighbors_agents):
                        agent_type = self.human_type

                agent = SocialMediaUser(self, agent_type=agent_type)
                self.grid.place_agent(agent, pos)
                self.schedule.add(agent)

        # Data collection
        self.datacollector = DataCollector(
            model_reporters={
                "total_human_disinformed": lambda m: sum(a.belief == 1 and a.type == 0 for a in m.schedule.agents),
                "total_human_informed": lambda m: sum(a.belief == 0 and a.type == 0 for a in m.schedule.agents),
                "disinfo_clusters": lambda m: m.count_disinfo_clusters(),
                "cumulative_clusters": lambda m: m.total_clusters,
                "happy_agents": lambda m: m.happy,
            },
            agent_reporters={
                "type": "type",
                "belief": "belief",
            },
        )
        self.datacollector.collect(self)

    def step(self):
        # Activate all agents in random order using the custom scheduler
        self.happy = 0
        self.schedule.step()
        self.datacollector.collect(self)

    def move_to_empty(self, agent):
        empty_cells = [pos for pos in self.grid.empties]
        if empty_cells:
            new_pos = random.choice(empty_cells)

            # Prevents bots from moving next to each other
            if (agent.type == self.bot_type):
                for new_pos in empty_cells:
                    neighbors = self.grid.get_neighborhood(new_pos, moore=True, include_center=False)
                    neighbor_agents = self.grid.get_cell_list_contents(neighbors)

                    if not any(agent.type == self.bot_type for agent in neighbor_agents):
                        self.grid.move_agent(agent, new_pos)
                        return 

            else:
                self.grid.move_agent(agent, new_pos)

    def count_disinfo_clusters(self):
        """
        Count clusters (echo chambers) of adjacent agents who have belief=1
        using a flood-fill approach.
        """
        visited = set()
        clusters = 0

        for _, pos in self.grid.coord_iter():
            cell_agents = self.grid.get_cell_list_contents(pos)
            if not cell_agents:
                continue
            agent = cell_agents[0]
            if agent.belief == 1 and pos not in visited:
                # Start a flood fill
                stack = [pos]
                while stack:
                    current_pos = stack.pop()
                    if current_pos in visited:
                        continue
                    visited.add(current_pos)
                    # Get neighbors
                    neighbors = self.grid.get_neighbors(
                        current_pos, moore=True, include_center=False
                    )
                    for neighbor in neighbors:
                        if neighbor.belief == 1 and neighbor.pos not in visited:
                            stack.append(neighbor.pos)
                clusters += 1
        
        self.total_clusters += clusters
        return clusters
