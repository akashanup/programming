"""
If we know the previous day on which the stock price was more than today then I can simply tell the stock span just by counting the number of days between today and the last day when stock price was more than today.
We just need to maintain a monotonic decreasing stack.

Create a stack which stores the last highest stock price and its span.
On every new day, if the stock price is lower than the last highest stock price then definitely it's span is 1 day.
But if the stock price is higher or equal to the last highest stock price then start checking the stack for a stock price which is higher than today's and once found than the span of today's stock price would be the sum of all intermediate spans.
"""


class StockSpanner:
    def __init__(self):
        self.stack = []

    def next(self, price: int) -> int:
        ans = 1
        while self.stack and self.stack[-1][0] <= price:
            ans += self.stack.pop()[1]

        self.stack.append([price, ans])
        return ans

# Your StockSpanner object will be instantiated and called as such:
# obj = StockSpanner()
# param_1 = obj.next(price)