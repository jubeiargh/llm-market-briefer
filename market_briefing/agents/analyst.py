from datetime import datetime, timezone
from langchain_core.messages import HumanMessage
from market_briefing.llm.executor import agent_executor
from market_briefing.workflow.state import BriefingState
import logging

logger = logging.getLogger(__name__)


def analyst_agent_node(state: BriefingState) -> dict:
    subject = state["subjects"][state["current_index"]]

    now = datetime.now(timezone.utc)
    from_time = now.replace(hour=0, minute=0, second=0, microsecond=0)
    to_time = from_time.replace(day=from_time.day + 1)

    iso_from = from_time.isoformat() + "Z"
    iso_to = to_time.isoformat() + "Z"

    prompt = f"""
    Summarize financial/political developments on '{subject}' in the last 24h (from {iso_from} to {iso_to}).
    Include what happened, market sentiment, and confidence if available. Keep it short.
    """

    logger.info(f"📤 Prompt to analyst agent:\n{prompt}")

    result = agent_executor.invoke({"messages": [HumanMessage(content=prompt)]})
    outputs = state.get("analyst_outputs", {})
    outputs[subject] = result["messages"][-1].content

    logger.info(f"📝 Final formatted briefing:\n{outputs[subject]}")

    return {"analyst_outputs": outputs}
