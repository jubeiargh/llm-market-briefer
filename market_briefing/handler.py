from market_briefing.config import SUBJECTS
from market_briefing.utils.html_formatter import markdown_to_html
from market_briefing.sender.email_sender import send_daily_email
from market_briefing.workflow.graph import build_graph
import logging

logging.basicConfig(level=logging.INFO)  # or INFO if DEBUG is too noisy


def main(event=None, context=None):
    state = {
        "subjects": SUBJECTS,
        "current_index": 0,
        "analyst_outputs": {},
    }

    graph = build_graph()
    result = graph.invoke(state)

    # Optionally log or persist somewhere (S3, email, etc.)
    print("✅ Morning Briefing Generated:\n", result["briefing"])

    briefing = result["briefing"]
    html = markdown_to_html(briefing)
    send_daily_email(html)

    return {"statusCode": 200, "briefing": result["briefing"]}
