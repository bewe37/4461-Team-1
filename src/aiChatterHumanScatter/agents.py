from mesa import Agent
import random

class SocialMediaUser(Agent):
    """
    A Schelling-style agent that includes a 'belief' attribute.
    agent_type = 1 => bot (always starts disinformed),
    agent_type = 0 => human (starts factual, can be flipped).
    """

    def __init__(self, model, agent_type: int):
        super().__init__(model)
        self.type = agent_type
        # Bots start disinformed (belief=1), humans start factual (belief=0)
        self.belief = 1 if agent_type == 1 else 0

    def step(self):
        
        # Get neighbors from the grid
        neighbors = self.model.grid.get_neighbors(
            self.pos, moore=True, include_center=False
        )
        if not neighbors:
            return
        if self.type == 1:
            # Calculate fraction of neighbors who are bots
            bot_neighbors = sum(1 for n in neighbors if n.type == 1)
            fraction_bots = bot_neighbors / len(neighbors)

            # If fewer than 50% of neighbors are bots, move
            if fraction_bots < 0.6:
                self.model.move_to_empty(self)

        else:
            # Count how many neighbors are bots
            bot_neighbors = sum(1 for n in neighbors if n.type == 1)

            # If there's at least one bot neighbor, adopt disinformation
            if bot_neighbors > 0:
                self.belief = 1

            # Otherwise, if there's a mix of beliefs, there's a 30% chance to switch
            else:
                same_belief = sum(1 for n in neighbors if n.belief == self.belief)
                diff_belief = len(neighbors) - same_belief
                if diff_belief > 0 and random.random() < 0.3:
                    self.belief = 0 if self.belief == 1 else 1


