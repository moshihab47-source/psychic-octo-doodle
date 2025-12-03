from dataclasses import dataclass
from src import config


@dataclass
class RiskState:
    daily_realized_profit: float = 0.0
    daily_realized_loss: float = 0.0
    trades_taken: int = 0


class RiskManager:
    """
    Tracks daily profit/loss and decides if we are allowed to keep trading.
    """

    def __init__(self):
        self.state = RiskState()

    def can_trade_today(self) -> bool:
        if self.state.daily_realized_profit >= config.DAILY_PROFIT_TARGET_USD:
            return False
        if self.state.daily_realized_loss <= -config.DAILY_MAX_LOSS_USD:
            return False
        return True

    def register_trade_result(self, pnl: float):
        """
        Update profit/loss after a trade closes.
        """
        self.state.trades_taken += 1
        if pnl >= 0:
            self.state.daily_realized_profit += pnl
        else:
            self.state.daily_realized_loss += pnl  # negative
