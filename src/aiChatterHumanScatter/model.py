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
    def __init__(
        self,
        height: int = 20,
        width: int = 20,
        density: float = 0.8,
        bot_ratio: float = 0.3,
        bot_influence: float = 0.5,
        seed=None,
    ):
        """
        :param height: Grid height
        :param width: Grid width
        :param density: Probability a cell is initially occupied
        :param bot_ratio: Fraction of agents that are bots
        :param bot_influence: Fraction of bot neighbors needed for a human to flip belief
        :param seed: Optional random seed
        """
        super().__init__(seed=seed)

        self.height = height
        self.width = width
        self.density = density
        self.bot_ratio = bot_ratio
        self.bot_influence = bot_influence
        self.total_clusters = 0

        # Initialize a SingleGrid 
        self.grid = SingleGrid(width, height, torus=True)

<<<<<<< HEAD
        # Initialize random activation scheduler
        self.schedule = RandomActivation(self)

        # Place agents and add them to the scheduler
=======
        # Initialize Random activation scheduler
        self.schedule = RandomActivation(self)

        # Place agents and add them to the scheduler
>>>>>>> b4546df73f29558b9eaddb889a3c839bd46451a0
        for _, pos in self.grid.coord_iter():
            if self.random.random() < self.density:
                # Decide agent type: 1=bot, 0=human
                agent_type = 1 if self.random.random() < self.bot_ratio else 0
                agent = SocialMediaUser(self, agent_type)
                self.grid.place_agent(agent, pos)
                self.schedule.add(agent)

        # Data collection
        self.datacollector = DataCollector(
            model_reporters={
                "total_human_disinfo": lambda m: sum(a.belief == 1 and a.type == 0 for a in m.schedule.agents),
                "disinfo_clusters": lambda m: m.count_disinfo_clusters(),
                "cumulative_clusters": lambda m: m.total_clusters,
            },
            agent_reporters={
                "type": "type",
                "belief": "belief",
            },
        )
        self.datacollector.collect(self)

    def step(self):
        # Activate all agents in random order using the custom scheduler
        self.schedule.step()
        self.datacollector.collect(self)

    def move_to_empty(self, agent):
        empty_cells = []
        for _, pos in self.grid.coord_iter():
            if len(self.grid.get_cell_list_contents(pos)) == 0:
                empty_cells.append(pos)
        if empty_cells:
            new_pos = random.choice(empty_cells)
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
