class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        left = 0
        
        initial_buy = prices[0]
        profit = 0
        while left < len(prices):
            if prices[left] < initial_buy:
                initial_buy = prices[left]
            else:
                profit = max(profit,prices[left]-initial_buy)
            left += 1
        return profit