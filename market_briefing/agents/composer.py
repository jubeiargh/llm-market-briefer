from datetime import datetime, timezone
from langchain_core.messages import HumanMessage
from market_briefing.llm.executor import agent_executor
import logging

logger = logging.getLogger(__name__)

# Phrases that likely indicate there's no real news
FALLBACK_PHRASES = [
    "unable to retrieve",
    "no information",
    "no articles",
    "if you'd like",
    "let me know how you'd like to proceed",
]


def is_meaningful_summary(summary: str) -> bool:
    summary_lower = summary.lower()
    return not any(phrase in summary_lower for phrase in FALLBACK_PHRASES)


def compose_briefing_node(state: dict) -> dict:
    now = datetime.now(timezone.utc).strftime("%B %d, %Y")

    logger.info("🧩 Composing final morning market briefing...")
    logger.info(f"📦 Current subjects and summaries: {state['analyst_outputs']}")


    joined_summaries = "\n\n".join(
        f"🔹 {subj}\n{summary.strip()}"
        for subj, summary in state["analyst_outputs"].items()
        if summary and isinstance(summary, str)
    )
    
    # Clear instruction for GPT to *only format*, not summarize away valid sections
    formatting_prompt = f"""
You are a professional financial news editor. Format the following topic summaries into a clean, well-presented morning market briefing.

✅ Do:
- Use headlines
- Add emojis and good spacing
- Improve clarity where needed
- Skip sections that have no information available
- Dont repeat yourself

🚫 Do not:
- Guess or fill in missing content
- Say anything unrelated to the actual summaries

🗓️ Date: {now}

{joined_summaries}
"""

    logger.info(f"📤 Prompt to composer agent:\n{formatting_prompt}")

    result = agent_executor.invoke(
        {"messages": [HumanMessage(content=formatting_prompt)]}
    )
    final_message = result["messages"][-1].content

    logger.info(f"📝 Final formatted briefing:\n{final_message}")

    return {"briefing": final_message}
