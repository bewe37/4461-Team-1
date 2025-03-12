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
        """
        Example logic:
          - If agent is a bot, move if fraction of neighbors who are also bots < 0.5.
          - If agent is a human, become disinformed if any bot neighbors exist.
        """
        # Get neighbors from the grid
        neighbors = self.model.grid.get_neighbors(
            self.pos, moore=True, include_center=False
        )
        if not neighbors:
            return

        if self.type == 1:
            # -----------------
            # BOT movement
            # -----------------
            bot_neighbors = sum(1 for n in neighbors if n.type == 1)
            fraction_bots = bot_neighbors / len(neighbors)
            # If fewer than 50% neighbors are bots, move
            if fraction_bots < 0.5:
                # NOTE: move_to_empty must be defined in your model!
                self.model.move_to_empty(self)
        else:
            # -----------------
            # HUMAN logic
            # -----------------
            bot_neighbors = sum(1 for n in neighbors if n.type == 1)
            # If there's at least one bot neighbor, adopt disinformation
            if bot_neighbors > 0:
                self.belief = 1
