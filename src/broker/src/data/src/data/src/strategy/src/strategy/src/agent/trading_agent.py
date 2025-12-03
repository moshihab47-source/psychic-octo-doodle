from src.broker.peo_pam_client import PeoPamClient, Order
from src.data.market_data import get_historical_data
from src.strategy.gold_silver_strategy import GoldSilverStrategy
from src.strategy.risk_manager import RiskManager
from src import config


class TradingAgent:
    def __init__(self, symbol: str = "XAUUSD"):
        self.symbol = symbol
        self.broker = PeoPamClient()
        self.strategy = GoldSilverStrategy(symbol)
        self.risk_manager = RiskManager()

    def run_once_backtest(self):
        """
        Simple test: get some recent data, ask the strategy for a signal,
        and print the result. Does NOT place any real trades.
        """
        df = get_historical_data(self.symbol, period="5d", interval=config.TIMEFRAME)
        signal = self.strategy.generate_signal(df)
        if signal:
            print(f"Signal: {signal.side.upper()} {signal.symbol} at {signal.entry_price}")
            print(f"  SL: {signal.stop_loss}  TP: {signal.take_profit}")
        else:
            print("No signal generated.")

    def submit_live_trade(self, signal):
        """
        Convert a TradeSignal into an Order and send to broker (currently PAPER).
        """
        order = Order(
            symbol=signal.symbol,
            side=signal.side,
            size=0.01,  # placeholder lot size
            entry_price=signal.entry_price,
            stop_loss=signal.stop_loss,
            take_profit=signal.take_profit,
        )
        order_id = self.broker.submit_order(order)
        print(f"Submitted order id: {order_id}")


if __name__ == "__main__":
    agent = TradingAgent(symbol="XAUUSD")
    agent.run_once_backtest()
