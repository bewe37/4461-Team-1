import solara

# Import the simplified Schelling model (with no homophily/happiness).
# Make sure this import points to your updated model file.
from model import Schelling

from mesa.visualization import (
    Slider,
    SolaraViz,
    make_plot_component,
    make_space_component,
)


def get_disinfo_stats(model):
    """
    Display the total number of agents who are disinformed.
    """
    total_human_disinformed = sum(a.belief == 1 and a.type == 0 for a in model.agents)
    total_human_informed = sum(a.belief == 0 and a.type == 0 for a in model.agents)
    total_clusters = model.total_clusters
    return solara.Markdown(
        f"**Total Disinformed Humans:** {total_human_disinformed}  \n"
        f"**Total Informed Humans:** {total_human_informed}  \n"
        f"**Total Disinfo Clusters:** {total_clusters} \n"
        f"**Happy Agents:** {model.happy}"

    )


def agent_portrayal(agent):
    """
      - Bots (user_type==1) are gray.
      - Humans (user_type==0) are green if factual (belief==0)
        and orange if disinformed (belief==1).
    """

    if agent.type == 1:
        color = "gray"
        marker = "s"
    else:
        color = "tab:green" if agent.belief == 0 else "tab:orange"
        marker = "o"
    return {"color": color, "marker": marker}


# Define model parameters for the Solara interface
model_params = {
    "seed": {
        "type": "InputText",
        "value": 42,
        "label": "Random Seed",
    },
    "density": Slider("Probability of a cell being occupied", 0.8, 0.1, 1.0, 0.1),
    "bot_ratio": Slider("Probabiliy of an agent being a bot", 0.1, 0.0, 1.0, 0.05),
    "bot_influence": Slider("Bot influence", 0.5, 0.0, 1.0, 0.05),
    "homophily": Slider("Homophily Threshold", value=0.5, min=0.0, max=1.0, step=0.05),
    "width": 20,
    "height": 20,
}

# Create a model instance
model1 = Schelling()

# Create a plot component showing total disinfo and cumulative clusters over time (from DataCollector)
DisinfoPlot = make_plot_component({"total_human_disinformed": "tab:red"})
InfoPlot = make_plot_component({"total_human_informed": "tab:red"})
ClustersPlot = make_plot_component({"cumulative_clusters": "tab:blue"})  
HappyPlot = make_plot_component({"happy_agents": "tab:green"})


# Build the SolaraViz page
page = SolaraViz(
    model1,
    components=[
        make_space_component(agent_portrayal),
        DisinfoPlot,
        InfoPlot,
        ClustersPlot,
        HappyPlot,  
        get_disinfo_stats,  
    ],
    model_params=model_params,
)

page  # noqa
