**Section 1:**

The chosen phenomenon of our group is the fabrication of Echo Chambers caused by interactions between bots on centralized social networking apps.   
One of the key dynamics we would like to hone in on is between the users and social media platforms, from the perspective of a user, who expects to use a platform to gain connections with other humans. Instead, users encounter bots who often have other objectives in mind when pushing certain posts and messages. This gives the impression that certain groups on a platform are larger or more influential than they are and creates a large active social media presence for them. These bots often consist of content creators and amplifiers.  
When the social media platform becomes saturated with discussion on extreme and/or opposing topics, users who disagree with the topics may choose to leave due to a lack of belongingness. Additionally, if a user can identify that they are interacting with bots, they may also choose to leave due to the platform not providing the reason for why they joined initially.

**Section 2:**

Hajli, N., Saeed, U., Tajvidi, M., & Shirazi, F. (2022). Social Bots and the Spread of Disinformation in Social Media: The Challenges of Artificial Intelligence. *British Journal of Management*, *33*(3), 1238–1253. [https://doi.org/10.1111/1467-8551.12554](https://doi.org/10.1111/1467-8551.12554)

This article looks into the general prevalence of bots on social media in an attempt to determine the intentions of the authors behind them. While the bots sometimes produce positive interactions, in most cases, bots will spread false information, attempt to incite or escalate arguments or sell/create scams. Despite users generally believing the information that bot accounts share less often than human accounts, bots are still commonly able to accelerate the spread of both true and false news, with fake news being the most effective topic to spread.

Hossein Nazer, T. (2019). *Understanding Bots on Social Media – An Application in Disaster Response*. ProQuest Dissertations & Theses.

This dissertation looks into the prevalence of bots on social media during disasters, both malicious and benign, and studies how to identify them, how users interact with them, and the harm that they cause. Hossein defines benign bots as usually being run by a reputable source, that self-identify as bots, and that provides useful information such as weather patterns or disaster alerts. These are in contrast to malicious bots, who often pretend to be human and will share information that tends to be falsified or shared to promote other topics. For example, they may create tweets tagged around both a current disaster and a current political topic, thus creating a connection between the two and drawing attention to their promoted opinion on that political topic. This can cause issues as information that could be vital to disaster response or learning about a current situation will be muddied by unrelated and often extreme political connections. They will also often try to “connect” with many more users than the average human does, spreading their information further.

**Section 3:**

The closest Mesa example to our phenomenon of echo chamber formation in social media is the Schelling Segregation Model, as it illustrates how individuals could become disengaged or segregated from the larger groups when exposed to a large amount of opposing content.

**3.1 Entities**

* Human Users  
  * Humans are the primary participants in the social media ecosystem. They actively engage in discussions and continuously communicate and make connections with others.  
  * Roles, Behaviors, and Goals:  
    * They tend to interact with others who share the same beliefs or perspectives.  
    * They leave or become disengaged when exposed to too many opposing contents   
    * They are commonly attracted by high-engagement content and content that aligns with their views, which oftentimes can be manipulated by bots.  
* Social Bots  
  * Social bots in social media can be categorized into two types; content-creation bots and content-amplifier bots.   
  * Roles, Behaviors, and Goals:  
    * Content-Creation  
      * Content creation bots behave like humans and they generate posts that promote specific viewpoints.   
    * Content-Amplifier  
      * Content amplifier bots share specific content to make it appear dominant.

In connection to the mesa models, generally, the nodes would represent views from human users on a platform. Within these nodes would be squares that represent bots who infiltrate these nodes and cause a shift in the size, as they create and amplify content that shifts the views of human users or causes them to leave a platform.

**3.2 Affordances**  
Through centralized social media platforms, numerous affordances arise that create action possibilities, potentially impacting data distribution and creating echo chambers. Affordances that content amplifiers would take advantage of include upvoting, liking, and reposting posts. These often appear as little symbols or icons within posts that are easy for users to identify their use and click, such as a heart or up arrow symbol. Content creation bots would use affordances such as hashtags, being adjudicated, and eliciting emotional responses. These affordances are typically in the form of posts which often have keywords to be easily discoverable by users. The goal of using these affordances is to manipulate data to appear that these posts are popular and highly enjoyed by many individuals, thus they should be spread to a larger audience to be viewed. Following the mesa examples, an analogy to represent this would be nodes that represent two opposing views, and one of the nodes outgrowing the other due to the “popularity” of the view as the bots skew data.

**3.3 Algorithms**  
Social media platforms rely on various algorithms to drive user engagement. 

* Recommendation Algorithms  
  * These algorithms analyze the user’s behaviour by tracking their past interactions to prioritize content that is aligned with the user’s preference. This simulates how agents in the Schelling Model prefer similar neighbours.  
* Content Prioritization  
  * The position of posts on social media is related to their engagement rank (likes, shares, and comments). As a result, popular content is always placed on the top, and bots could exploit this by amplifying certain narratives, making them appear more dominant. This mirrors how external factors in the Schelling model accelerate segregation by influencing agent movement.

**Section 4:**  
![][image1]

Above is a sample output based on the Schelling Segregation Model, roughly representing our goal for the simulation we make based on Schelling

**GREEN nodes** represent humans with opinion A about a topic  
**PURPLE nodes** represent humans with opinion B about a topic  
**RED SQUARED** nodes represent bots that are perpetrating those opinions

In this example, **PURPLE** may have originally been a minority opinion, which grew as people saw the bots sharing it, making it seem more popular than it was. Areas with high bot concentration would have seen users leave the platform, and new users just joining the platform are more likely to do so because they share the popular opinion. Bots would self-sort to not overlap with each other in most cases, and not be near each other, while also promoting the opinions they are created to promote.

[image1]: <data:image/png;base64,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>