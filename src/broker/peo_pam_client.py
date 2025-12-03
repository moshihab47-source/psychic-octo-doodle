from dataclasses import dataclass
from typing import List, Dict
from src import config


@dataclass
class Order:
    symbol: str
    side: str           # "buy" or "sell"
    size: float
    entry_price: float
    stop_loss: float
    take_profit: float


class PeoPamClient:
    """
    Wrapper around the PEO PAM / broker API.

    Currently this is only a skeleton and does NOT connect to any real account.
    Later we will replace the internal methods with real HTTP / SDK calls.
    """

    def __init__(self):
        self.api_key = config.PEO_PAM_API_KEY
        self.api_secret = config.PEO_PAM_API_SECRET
        self.account_id = config.PEO_PAM_ACCOUNT_ID

    # ---------- ACCOUNT ---------- #
    def get_balance(self) -> float:
        """
        Return available balance in USD.
        Currently returns a dummy value for testing.
        """
        # TODO: call real API here
        return 1000.0

    # ---------- ORDERS ---------- #
    def submit_order(self, order: Order) -> str:
        """
        Submit a new market order with SL and TP.
        Returns an order id (dummy for now).
        """
        # TODO: implement real API call
        print(f"[PAPER] Submitting order: {order}")
        return "dummy-order-id"

    def get_open_positions(self) -> List[Dict]:
        """
        Returns current open positions.
        """
        # TODO: implement real API call
        return []

    def close_all_positions(self):
        """
        Closes all open positions. For safety / end-of-day logic.
        """
        # TODO: implement real API call
        print("[PAPER] Closing all positions")
