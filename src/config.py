import os
from dotenv import load_dotenv

load_dotenv()

# Daily trading allocation & limits
DAILY_ALLOCATION_USD = 100.0
DAILY_PROFIT_TARGET_USD = 15.0
DAILY_MAX_LOSS_USD = 15.0

SYMBOLS = ["XAUUSD", "XAGUSD"]

# Risk settings
RISK_PER_TRADE_USD = 4.0
TAKE_PROFIT_R_MULTIPLE = 1.8

# Timeframe for analysis
TIMEFRAME = "15m"

# Broker credentials (later)
PEO_PAM_API_KEY = os.getenv("PEO_PAM_API_KEY", "")
PEO_PAM_API_SECRET = os.getenv("PEO_PAM_API_SECRET", "")
PEO_PAM_ACCOUNT_ID = os.getenv("PEO_PAM_ACCOUNT_ID", "")

PAPER_TRADING = True
