from mesa import Agent
import random

class SocialMediaUser(Agent):
    """
    A social media user in an echo chamber model.
    user_type = 1 => bot, user_type = 0 => human
    belief = 1 => disinformed, belief = 0 => factual
    """

    def __init__(self, unique_id, model, user_type: int):
        # Initialize the base Agent class.
        self.unique_id = unique_id
        self.model = model
        self.user_type = user_type
        
        # Bots always start disinformed (1)
        if user_type == 1:
            self.belief = 1
        else:
            # Humans start with a random belief: factual (0) or disinformed (1)
            self.belief = 0

        self.pos = None

    def step(self) -> None:
        """
        Update belief based on the influence of neighbors.
        Bots do not update their beliefs.
        Humans may update their belief when exposed to bot neighbors or mixed exposure.
        """
        neighbors = self.model.grid.get_neighbors(
            self.pos, moore=True, include_center=False
        )

        # If there are no neighbors or if the agent is a bot, do nothing.
        if not neighbors or self.user_type == 1:
            return

        # Count neighbors with the same belief.
        same_belief = sum(1 for n in neighbors if n.belief == self.belief)
        diff_belief = len(neighbors) - same_belief
        
        # Count bot neighbors.
        bot_neighbors = sum(1 for n in neighbors if n.user_type == 1)

        # Bots strongly influence their neighbors toward disinformation.
        if bot_neighbors > 0:
            self.belief = 1
        # If there is mixed exposure, allow a 30% chance to switch belief.
        elif diff_belief > 0 and random.random() < 0.3:
            self.belief = 0 if self.belief == 1 else 1
