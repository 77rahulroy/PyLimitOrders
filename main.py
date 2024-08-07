from trading_framework.execution_client import ExecutionClient, ExecutionException
from limit.limit_order_agent import LimitOrderAgent

class MockExecutionClient:
    def buy(self, product_id: str, amount: int):
        if amount <= 0:
            raise ExecutionException("Amount must be positive")
        print(f"Buying {amount} shares of {product_id}")

    def sell(self, product_id: str, amount: int):
        if amount <= 0:
            raise ExecutionException("Amount must be positive")
        print(f"Selling {amount} shares of {product_id}")

if __name__ == "__main__":
    execution_client = MockExecutionClient()
    agent = LimitOrderAgent(execution_client)
    agent.add_order('buy', 'IBM', 1000, 100)

    # Simulate price ticks
    agent.on_price_tick('IBM', 99)  # Should trigger the buy order
    agent.on_price_tick('IBM', 101) # Should not trigger any order
