import solara

from model import EchoChamberModel
from mesa.visualization import (
    Slider,
    SolaraViz,
    make_plot_component,
    make_space_component,
)

def get_disinfo_stats(model):
    """
    Display disinformation statistics.
    """
    total_disinfo = model.get_total_disinfo()
    human_disinfo = model.get_human_disinfo()
    clusters = model.count_disinfo_clusters()
    return solara.Markdown(
        f"**Total disinfo agents:** {total_disinfo}  |  **Human disinfo:** {human_disinfo}  |  **Echo Chambers:** {clusters}"
    )

def agent_portrayal(agent):
    """
    Set colors for agents:
      - Bots (user_type==1) are blue.
      - Humans (user_type==0) are green if factual (belief==0)
        and orange if disinformed (belief==1).
    """
    if agent.user_type == 1:
        color = "tab:blue"
    else:
        color = "tab:green" if agent.belief == 0 else "tab:orange"
    return {"color": color}

# Model parameters with interactive sliders/inputs.
model_params = {
    "seed": {
        "type": "InputText",
        "value": 42,
        "label": "Random Seed",
    },
    "density": Slider("Agent density", 0.8, 0.1, 1.0, 0.1),
    "bot_ratio": Slider("Bot ratio", 0.3, 0.0, 1.0, 0.05),
    "influence_threshold": Slider("Influence Threshold", 0.6, 0.0, 1.0, 0.05),
    "width": 20,
    "height": 20,
}

# Create an instance of the EchoChamberModel.
model_instance = EchoChamberModel()

# Create a plot component showing total disinformation over time.
DisinfoPlot = make_plot_component({"total_disinfo": "tab:green"})

# Create the SolaraViz page.
page = SolaraViz(
    model_instance,
    components=[
        make_space_component(agent_portrayal),
        DisinfoPlot,
        get_disinfo_stats,
    ],
    model_params=model_params,
)

page  # noqa
