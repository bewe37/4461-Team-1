from mesa import Agent
import random

class SocialMediaUser(Agent):
    """
    A Schelling-style agent with a 'belief' attribute.
    type = 1 => disinformed/disinformational, type = 0 => informed/informational.
    """

    human_type = 0
    bot_type = 1
    informed_type = 0
    disinformed_type = 1

    def __init__(self, model, agent_type: int):
        super().__init__(model)
        self.type = agent_type
        # 30% chance for a bot to be informational
        # Humans start informed
        if agent_type == self.bot_type:
            self.belief = self.informed_type if random.random() < 0.3 else self.disinformed_type
        else: 
            self.belief = self.informed_type

        self.step_counter = -1 # Counter to track steps

    def step(self):
        neighbors = self.model.grid.get_neighbors(self.pos, moore=True, include_center=False)
        if not neighbors:
            return

        if self.type == self.bot_type:
            # BOT behavior
            # Can move once human neighbor shares belief
            if any(n.type == self.human_type and n.belief == self.belief for n in neighbors) and self.step_counter % 2 == 0:
                self.model.move_to_empty(self)

        else:
            # HUMAN behavior
            if self.belief == self.informed_type:
                opposite_type = self.disinformed_type
            else:
                opposite_type = self.informed_type

            # If there's at least one bot neighbor, chance humans belief changes.
            if any(n.type == self.bot_type and n.belief == opposite_type for n in neighbors) and random.random() < self.model.bot_influence:
                self.belief = opposite_type

            same_belief_neighbors = sum(1 for n in neighbors if n.belief == self.belief)
            similarity_fraction = same_belief_neighbors / len(neighbors)

            if similarity_fraction < self.model.homophily:
                # Chance to move if unhappy
                if self.step_counter % 2 == 0:
                    self.model.move_to_empty(self)
            else:
                # Agent is happy, increment the model's happy counter
                self.model.happy += 1

        self.step_counter += 1
