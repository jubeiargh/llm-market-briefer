from market_briefing.handler import main
from market_briefing.utils.html_formatter import markdown_to_html
from market_briefing.sender.email_sender import send_daily_email
from market_briefing.workflow.graph import build_graph
import logging

logging.basicConfig(level=logging.INFO)  # or INFO if DEBUG is too noisy


if __name__ == "__main__":
    main()
