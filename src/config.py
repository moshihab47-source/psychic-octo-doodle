import os
from dotenv import load_dotenv

# Load environment variables from .env file if present
load_dotenv()

# --- GENERAL SETTINGS --- #
DAILY_ALLOCATION_USD = 100.0       # capital to use per day
DAILY_PROFIT_TARGET_USD = 15.0     # stop trading once this profit is reached
DAILY_MAX_LOSS_USD = 15.0          # stop trading once this loss is reached

SYMBOLS = ["XAUUSD", "XAGUSD"]     # gold and silver

RISK_PER_TRADE_USD = 4.0           # max loss per trade
TAKE_PROFIT_R_MULTIPLE = 1.8       # TP ~1.8x the risk (e.g., risk $4 to make $7.2)

TIMEFRAME = "15m"                  # placeholder time frame

# --- BROKER / PEO PAM --- #
PEO_PAM_API_KEY = os.getenv("PEO_PAM_API_KEY", "")
PEO_PAM_API_SECRET = os.getenv("PEO_PAM_API_SECRET", "")
PEO_PAM_ACCOUNT_ID = os.getenv("PEO_PAM_ACCOUNT_ID", "")

# Paper trading flag: NEVER set this False until you are sure
PAPER_TRADING = True

