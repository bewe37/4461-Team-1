import random
from mesa import Agent

class SocialMediaUser(Agent):
    """
    Schelling-style agent:
      type=1 ⇒ bot, type=0 ⇒ human
      belief=0 ⇒ factual (informed), belief=1 ⇒ misinformed (disinformed)
    """
    human_type = 0
    bot_type = 1
    informed_type = 0
    disinformed_type = 1

    def __init__(self, model, agent_type: int):
        super().__init__(model)
        self.type = agent_type
        # Bots start misinformed 70% of the time, factual 30%
        if agent_type == self.bot_type:
            self.belief = self.informed_type if random.random() < 0.3 else self.disinformed_type
            self.activated = False
        else:
            self.belief = self.disinformed_type if random.random() < 0.2 else self.informed_type
            self.activated = True
        self.step_counter = 0

    def step(self):
        neighbors = self.model.grid.get_neighbors(self.pos, moore=True, include_center=False)
        if not neighbors:
            self.step_counter += 1
            return

        if self.type == self.bot_type:
            # Bots act only during disasters
        
            if self.model.in_disaster:
                if any(n.type == self.human_type and n.belief == self.belief for n in neighbors) and self.step_counter % 2 == 0:
                    self.model.move_to_empty(self)

        else:
            # Human-to-human spread disinformation to other humans before disaster
            if not self.model.in_disaster:
                for neighbor in neighbors:
                    if neighbor.type == self.human_type and neighbor.belief != self.belief and random.random() < 0.15:
                        neighbor.belief = self.belief
                        if self.belief == self.disinformed_type:
                            self.model.informed_humans_converted += 1
                        else:
                            self.model.disinformed_humans_converted += 1

            # Adoption from bots if exposed
            if self.belief == self.informed_type:
                opposite_type = self.disinformed_type
            else:
                opposite_type = self.informed_type

            # If there's at least one bot neighbor, chance humans belief changes.
            if any(n.type == self.bot_type and n.belief == opposite_type for n in neighbors) and random.random() < self.model.bot_influence:
                self.belief = opposite_type

                if self.belief == self.disinformed_type:
                    self.model.informed_humans_converted += 1
                else:
                    self.model.disinformed_humans_converted += 1

            # Movement & happiness: more sporadic during disaster
            same = sum(1 for n in neighbors if n.belief == self.belief)
            frac = same / len(neighbors)
            move_prob = 0.5 if self.model.in_disaster else 0.1
            if frac < self.model.homophily and self.step_counter % 2 == 0:
                self.model.move_to_empty(self)
            else:
                self.model.happy += 1
                if random.random() < move_prob:
                    self.model.move_to_empty(self)

        self.step_counter += 1
