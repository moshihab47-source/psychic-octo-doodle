import yfinance as yf
import pandas as pd


def get_historical_data(
    symbol: str,
    period: str = "30d",
    interval: str = "15m"
) -> pd.DataFrame:
    """
    Fetch historical OHLCV data for a symbol using yfinance.
    This is used for testing/backtesting, not live.
    """
    # Metals often use =X suffix on Yahoo Finance
    yahoo_symbol = symbol + "=X" if symbol in ("XAUUSD", "XAGUSD") else symbol

    ticker = yf.Ticker(yahoo_symbol)
    df = ticker.history(period=period, interval=interval)

    df = df.rename(
        columns={
            "Open": "open",
            "High": "high",
            "Low": "low",
            "Close": "close",
            "Volume": "volume",
        }
    )

    return df.dropna()


def get_latest_price(symbol: str) -> float:
    """
    Get the most recent close price for a symbol.
    """
    df = get_historical_data(symbol, period="1d", interval="1m")
    return float(df["close"].iloc[-1])
