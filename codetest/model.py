import random
from mesa import Model
from mesa.space import SingleGrid
from mesa.datacollection import DataCollector
from agents import SocialMediaUser


class CustomScheduler:
    """
    A simple custom scheduler that shuffles agents randomly each step.
    """
    def __init__(self, model):
        self.model = model
        self.agents = []

    def add(self, agent):
        self.agents.append(agent)

    def step(self):
        random.shuffle(self.agents)
        for agent in self.agents:
            agent.step()


class EchoChamberModel(Model):
    """
    A model where bot-to-bot interactions create echo chambers,
    spreading disinformation to human agents.
    """
    def __init__(
        self,
        width=20,
        height=20,
        density=0.8,             # fraction of cells occupied
        bot_ratio=0.3,           # fraction of agents that are bots
        influence_threshold=0.6, # probability that a human flips to disinfo if exposed to a disinfo bot
        seed=None,
    ):
        """
        Create a new EchoChamberModel.
        :param width: Grid width
        :param height: Grid height
        :param density: Probability of placing an agent in each cell
        :param bot_ratio: Fraction of total agents that are bots
        :param influence_threshold: Probability that a human adopts disinfo from a bot
        :param seed: Random seed
        """
        super().__init__(seed=seed)
        self.width = width
        self.height = height
        self.density = density
        self.bot_ratio = bot_ratio
        self.influence_threshold = influence_threshold

        # Track unique agent IDs and simulation steps
        self._next_id = 0
        self.step_count = 0

        # Initialize grid and custom scheduler
        self.grid = SingleGrid(width, height, torus=True)
        self.schedule = CustomScheduler(self)

        # Calculate total agents and number of bots
        total_cells = width * height
        total_agents = int(total_cells * density)
        bot_count = int(total_agents * bot_ratio)

        # Place agents manually on the grid using two-element unpacking
        for _, pos in self.grid.coord_iter():
            if self.random.random() < self.density:
                # If bot_count is still positive, create a bot; otherwise, create a human.
                user_type = 1 if bot_count > 0 else 0
                agent = SocialMediaUser(self.next_id(), self, user_type)
                self.schedule.add(agent)
                self.grid.place_agent(agent, pos)

                # Decrement bot_count only if a bot is placed.
                if user_type == 1:
                    bot_count -= 1

        # Initialize data collection after all agents are placed.
        self.datacollector = DataCollector(
            model_reporters={
                "total_disinfo": lambda m: sum(a.belief == 1 for a in m.schedule.agents),
                "human_disinfo": lambda m: sum(a.belief == 1 and a.user_type == 0 for a in m.schedule.agents),
                "disinfo_clusters": lambda m: m.count_disinfo_clusters(),
            }
        )
        self.datacollector.collect(self)

    def next_id(self):
        """Return the next unique ID."""
        self._next_id += 1
        return self._next_id

    def step(self):
        """Advance the model by one step."""
        self.schedule.step()
        self.datacollector.collect(self)
        self.step_count += 1
        print(f"Model step {self.step_count}, total_disinfo={self.get_total_disinfo()}")

    def get_total_disinfo(self):
        """Count total number of agents spreading disinformation."""
        return sum(1 for a in self.schedule.agents if a.belief == 1)

    def get_human_disinfo(self):
        """Count total number of humans who believe disinformation."""
        return sum(1 for a in self.schedule.agents if a.belief == 1 and a.user_type == 0)

    def count_disinfo_clusters(self):
        """
        Count clusters (echo chambers) of adjacent agents with disinformed beliefs.
        Uses a flood-fill approach over the grid.
        Returns:
            An integer count of distinct disinformation clusters.
        """
        visited = set()
        clusters = 0

        # Iterate over each cell in the grid.
        for _, pos in self.grid.coord_iter():
            x, y = pos
            cell_contents = self.grid.get_cell_list_contents(pos)
            if cell_contents:
                agent = cell_contents[0]
                # Process only disinformed agents that haven't been visited.
                if agent.belief == 1 and (x, y) not in visited:
                    # Start a flood fill from this cell.
                    stack = [(x, y)]
                    while stack:
                        cx, cy = stack.pop()
                        if (cx, cy) in visited:
                            continue
                        visited.add((cx, cy))
                        agents_here = self.grid.get_cell_list_contents((cx, cy))
                        if agents_here and agents_here[0].belief == 1:
                            # Check all eight neighbors (Moore neighborhood with torus wrapping)
                            for dx in [-1, 0, 1]:
                                for dy in [-1, 0, 1]:
                                    if dx == 0 and dy == 0:
                                        continue
                                    nx = (cx + dx) % self.width
                                    ny = (cy + dy) % self.height
                                    if (nx, ny) not in visited:
                                        neighbor_agents = self.grid.get_cell_list_contents((nx, ny))
                                        if neighbor_agents and neighbor_agents[0].belief == 1:
                                            stack.append((nx, ny))
                    clusters += 1
        return clusters
