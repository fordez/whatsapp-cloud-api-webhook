import os
import logging

# Environment variables
VERIFY_TOKEN = os.getenv("VERIFY_TOKEN", "fordez-token")
APP_SECRET = os.getenv("APP_SECRET", "70720febab2dbef2ce140e672fcfd665")

# Logging setup
logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s"
)
logger = logging.getLogger(__name__)
