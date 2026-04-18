class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        buyPointer = 0
        sellPointer = 1
        maxProfit = 0

        for p in prices:
            if sellPointer > len(prices) - 1:
                break
            elif prices[sellPointer] < prices[buyPointer]:
                buyPointer = sellPointer
            profit = prices[sellPointer] - prices[buyPointer]
            maxProfit = max(maxProfit, profit)
            sellPointer+=1

        return maxProfit


            
