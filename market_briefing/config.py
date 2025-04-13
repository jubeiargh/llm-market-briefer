from dotenv import load_dotenv
import os

load_dotenv()

OPEN_AI_API_KEY = os.environ["OPEN_AI_API_KEY"]
FINLIGHT_API_KEY = os.environ["FINLIGHT_API_KEY"]
EMAIL_USER = os.getenv("EMAIL_USER")
EMAIL_PASS = os.getenv("EMAIL_PASS")
EMAIL_TO = os.getenv("EMAIL_TO")
EMAIL_SUBJECT = os.getenv("EMAIL_SUBJECT", "Daily Email")

SUBJECTS = ["Trump tariffs", "Nvidia", "ECB policy"]
