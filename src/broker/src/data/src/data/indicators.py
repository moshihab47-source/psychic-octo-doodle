import pandas as pd
import numpy as np


def ema(series: pd.Series, period: int = 20) -> pd.Series:
    """
    Exponential moving average.
    """
    return series.ewm(span=period, adjust=False).mean()


def rsi(series: pd.Series, period: int = 14) -> pd.Series:
    """
    Relative Strength Index (RSI).
    """
    delta = series.diff()
    gain = np.where(delta > 0, delta, 0.0)
    loss = np.where(delta < 0, -delta, 0.0)

    gain_ema = pd.Series(gain).ewm(span=period, adjust=False).mean()
    loss_ema = pd.Series(loss).ewm(span=period, adjust=False).mean()

    rs = gain_ema / (loss_ema + 1e-9)
    rsi_values = 100 - (100 / (1 + rs))
    return pd.Series(rsi_values, index=series.index)
