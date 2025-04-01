# §A. Overview of the Phenomenon
Our project focuses on the fabrication of echo chambers created from interactions between bots on X regarding discussions of current real-world disasters. We particularly highlight how bots manipulate users seeking information by spreading disinformation during this vulnerable time, leading users to believe the content they see is accurate. The disinformation includes posts with statistics such as the number of deaths, falsely AI-generated images, and fabricated rescue efforts, which could heavily trigger a user to show various signs of sympathy based on the seriousness of the content. 

In our project, the grid where agents populate represents X and their black-boxed recommendation algorithms. Agents can exist as either human users or bot users on X, where each agent is given a knowledge type. For bots, the knowledge type indicates disinformational or informational, whereas for human agents, it would represent those who are informed or disinformed. Additionally, human agents are dynamic and can change their knowledge type throughout the simulation, representing them becoming informed or disinformed as they interact with other users on X. Ultimately, the objective of bots is to influence humans based on their knowledge type, and humans will move around X to be with users who share their knowledge type.

We aim to display how the media ecosystem of X changes once a disaster occurs, and how quickly bots are able to appear on the platform to spread disinformation and drastically sway the opinions of humans. Overall, this has long-term impacts on the platform due to the dominance of disinformational bots over informational bots, ultimately creating large echo chambers of disinformed users. Because breaking into echo chambers is challenging due to opposing viewpoints, the platform has the potential to become oversaturated with disinformation.

---------------------------------------------------------------

# §B. How to run the simulation (installation steps, commands)
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

# §C. Key Findings
Bots will use numerous techniques to prevent being detected and removed, such as interacting with one another to auto-sort. Auto sorting includes mimicking human behaviour, altering posting locations, changing account attributes, randomizing interactions, bot diffusion, and dispersal once clusters are formed.  These interactions curate sock puppet accounts, where fake personas are constructed to make these accounts appear human-like and trustworthy. As these bots avoid detection,  disinformation bots also interact with the recommendation algorithms on X, where they deceive the algorithms by using numerous techniques that make the platform’s algorithms believe that their content is popular. A technique used is latching trending hashtags and keywords onto their messages to push them higher in the social media search results. During disasters, these trending hashtags and keywords are typically related to the present disaster event and have many more eyes on them than most other hashtags due to people wanting to seek information. Posts containing misinformation made by the bots are then spread throughout the media ecosystem to consumers by recommendation algorithms. Users engage with the posts because they are designed to evoke strong emotions, encouraging users to share, like, or repost, which drives analytics for the recommendation algorithms to detect. This interaction falls within another technique called engagement farming. The recommendation algorithms then further push the bot-driven disinformation alongside new posts potentially made by causally misinformed humans. This creates a feedback loop of disinformation through bots, recommendation algorithms, and human users. Resultantly, we display the long-term and hard-to-reverse effects of echo chambers on a platform.

In our simulation, we display numerous techniques of autosorting. The bot agents exhibit bot diffusion by avoiding spawning or moving near one another, making them appear as individual human users rather than coordinated groups. Additionally, bots will not stay in one part of the platform for too long and will move around randomly to mimic dispersal and alter posting locations. Through none of the bots leaving the simulation, we represent the algorithm not being able to detect the bots by none of the bots leaving the simulation. Additionally, as our simulation cycles through periods of disasters and non-disasters, we display how the simulation can never revert to how it was initially and that spreading disinformation and creating echo chambers is almost inevitable.
