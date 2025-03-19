# §A. Overview of the current implementation state.
Our current model consists of two agent types: humans and bots. Additionally, each agent has two knowledge types: informational/informed and 
disinformational/disinformed. The user is able to adjust sliders that impact the probablity of a cell being occupied on a grid, the probability
of an agent being a bot, the probability of a bot influencing an agent, and how high a bot's homophily has to be in order for it to remain in its
spot and not move. 

Agents move every other step, in order to see how human knowledge types can change based on a neighbouring bot possibly influencing it. Humans will 
move if they are not happy enough, based on whether neighbouring agents share the same knowledge type or not. Bots will only move once it has influenced
a neighbour, however, will not move or be placed next to each other to mimic autosorting. Overtime, echo chambers are created as humans move and stay to 
be around like minded neighbours.

---------------------------------------------------------------

# §B. How to run the simulation (installation steps, commands).
Ensure that you have the latest version of python installed
https://www.python.org/downloads/

Navigate to the directory where the 4461-Team-1 folder is installed through the terminal:
    for example: cd Users\yourUsername\Downloads\4461-Team-1

Install the dependencies by running:
    pip install -r requirements.txt

Navigate to the src file where the code is located:
    cd src/aiChatterHumanScatter

 Once on the directory, run the following command:
    solara run app.py

---------------------------------------------------------------

# §C. Limitations and planned improvements for the next phase.
A current limitation is connecting our model to specifically represent disasters, rather than just the spread of disinformation and information on a
platform in general. Resultantly, we plan to include active times for disasters that users can trigger, where bots would be placed into the model and
take advantage of humans within this sensitive state to influence them. Else, during inactive times of disasters, only humans would be able to influence
one another and bots would not be present. With this specific disaster system implemented, we hope to change other conditions such as human agents moving
regardless of their happiness due to a sense of panic, and providing bot agents with a significantly higher chance of influencing and misinforming them.
We could also experiment with the possibility of bot agents and human agents being removed and replaced, due to either bots being detected by the platform
or human agents leaving a platform due to the disinformation.
