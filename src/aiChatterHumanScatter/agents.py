from mesa import Agent
import random

class SocialMediaUser(Agent):
    """
    A Schelling-style agent with a 'belief' attribute.
    type = 1 => bot (disinformed), type = 0 => human (initially factual).
    """

    def __init__(self, model, agent_type: int):
        super().__init__(model)
        self.type = agent_type
        # 30% of bots started as disinformed, 70% informed / factual
        # Humans start factual (belief=0).
        if agent_type == 1:
            self.belief = 0 if random.random() < 0.3 else 1
            self.activated = False 
        else: 
            self.belief = 0
            self.activated = True

        self.activated = False if agent_type == 1 else True

    def step(self):
   
        neighbors = self.model.grid.get_neighbors(self.pos, moore=True, include_center=False)
        if not neighbors:
            return

        if self.type == 1:
            # BOT behavior
            if not self.activated:
                # Activate only if a neighbor human becomes misinformed
                if any(n.type == 0 and n.belief == 1 for n in neighbors):
                    self.activated = True
            else:
                bot_neighbors = sum(1 for n in neighbors if n.type == 1)
                fraction_bots = bot_neighbors / len(neighbors)

                # If fewer than 50% of neighbors are bots, move
                if fraction_bots < 0.5:
                    self.model.move_to_empty(self)
                
                # 30% chance of the bots spreading factual information
                for neighbor in neighbors:
                    if neighbor.type == 0:
                        neighbor.belief = 0 if random.random() < 0.3 else 1
        else:
            # HUMAN behavior
            bot_neighbors = sum(1 for n in neighbors if n.type == 1)
            # If there's at least one bot neighbor, humans exposed to misinformation.
            if bot_neighbors > 0 and random.random() < 0.3:
                self.belief = 1

            same_belief_neighbors = sum(1 for n in neighbors if n.belief == self.belief)
            similarity_fraction = same_belief_neighbors / len(neighbors)

            if similarity_fraction < self.model.homophily:
                # 50% chance to leave the ecosystem
                self.model.move_to_empty(self)
            else:
                # Agent is happy, increment the model's happy counter
                self.model.happy += 1
