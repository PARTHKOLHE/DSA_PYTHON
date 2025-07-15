from typing import List
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        mina = float('inf')
        max_profit = 0
        
        for price in prices:
            if price < mina:
                mina = price
            
            elif price - mina > max_profit:
                max_profit = price - mina
        return max_profit
                    
        
            