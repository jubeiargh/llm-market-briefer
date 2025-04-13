from langgraph.graph import StateGraph, END
from market_briefing.workflow.state import BriefingState
from market_briefing.agents.analyst import analyst_agent_node
from market_briefing.agents.composer import compose_briefing_node


def increment_index_node(state: BriefingState) -> dict:
    return {"current_index": state["current_index"] + 1}


def should_continue(state: BriefingState) -> str:
    return (
        "continue" if state["current_index"] + 1 < len(state["subjects"]) else "format"
    )


def build_graph():
    graph = StateGraph(BriefingState)

    graph.add_node("analyst", analyst_agent_node)
    graph.add_node("increment_index", increment_index_node)
    graph.add_node("composer", compose_briefing_node)

    graph.add_conditional_edges(
        "analyst",
        should_continue,
        {"continue": "increment_index", "format": "composer"},
    )

    graph.add_edge("increment_index", "analyst")
    graph.set_entry_point("analyst")
    graph.add_edge("composer", END)

    return graph.compile()
