from dataclasses import dataclass
from typing import Optional
import pandas as pd

from src.data.indicators import ema, rsi
from src import config


@dataclass
class TradeSignal:
    symbol: str
    side: str       # "buy" or "sell"
    entry_price: float
    stop_loss: float
    take_profit: float


class GoldSilverStrategy:
    """
    Very simple starter strategy for gold/silver:
    - Uses EMA trend and RSI.
    - BUY: uptrend + oversold.
    - SELL: downtrend + overbought.
    """

    def __init__(self, symbol: str = "XAUUSD"):
        self.symbol = symbol

    def generate_signal(self, df: pd.DataFrame) -> Optional[TradeSignal]:
        if len(df) < 60:
            return None  # not enough data

        close = df["close"]
        ema_fast = ema(close, period=20)
        ema_slow = ema(close, period=50)
        rsi_14 = rsi(close, period=14)

        last_price = float(close.iloc[-1])
        last_ema_fast = float(ema_fast.iloc[-1])
        last_ema_slow = float(ema_slow.iloc[-1])
        last_rsi = float(rsi_14.iloc[-1])

        # BUY when uptrend + RSI oversold
        if last_ema_fast > last_ema_slow and last_rsi < 35:
            risk = config.RISK_PER_TRADE_USD
            sl = last_price - (risk / 10)   # placeholder
            tp = last_price + (risk * config.TAKE_PROFIT_R_MULTIPLE / 10)
            return TradeSignal(
                symbol=self.symbol,
                side="buy",
                entry_price=last_price,
                stop_loss=sl,
                take_profit=tp,
            )

        # SELL when downtrend + RSI overbought
        if last_ema_fast < last_ema_slow and last_rsi > 65:
            risk = config.RISK_PER_TRADE_USD
            sl = last_price + (risk / 10)
            tp = last_price - (risk * config.TAKE_PROFIT_R_MULTIPLE / 10)
            return TradeSignal(
                symbol=self.symbol,
                side="sell",
                entry_price=last_price,
                stop_loss=sl,
                take_profit=tp,
            )

        return None
