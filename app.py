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
    total_disinfo = sum(a.belief == 1 for a in model.agents)
    return solara.Markdown(f"**Total Disinfo Agents:** {total_disinfo}")


def agent_portrayal(agent):
    """
     Set colors for agents:
      - Bots (user_type==1) are blue.
      - Humans (user_type==0) are green if factual (belief==0)
        and orange if disinformed (belief==1).
    """

    if agent.type == 1:
        color = "tab:blue"
    else:
        color = "tab:green" if agent.belief == 0 else "tab:orange"
    return {"color": color}


# Define model parameters for the Solara interface
model_params = {
    "seed": {
        "type": "InputText",
        "value": 42,
        "label": "Random Seed",
    },
    "density": Slider("Agent density", 0.8, 0.1, 1.0, 0.1),
    "bot_ratio": Slider("Bot ratio", 0.3, 0.0, 1.0, 0.05),
    "bot_influence": Slider("Bot influence", 0.5, 0.0, 1.0, 0.05),
    "width": 20,
    "height": 20,
}

# Create a model instance
model1 = Schelling()

# Create a plot component showing total disinfo over time (from DataCollector)
DisinfoPlot = make_plot_component({"total_disinfo": "tab:red"})

# Build the SolaraViz page
page = SolaraViz(
    model1,
    components=[
        make_space_component(agent_portrayal),
        DisinfoPlot,
        get_disinfo_stats,
    ],
    model_params=model_params,
)

page  # noqa
