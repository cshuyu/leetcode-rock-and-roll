# Last updated: 2/23/2026, 6:46:40 PM
class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        # d[i][w] is the number of combinations with coins [0:i] and the amount is w.
        # Rules:
        # d[i][w] = d[i-1][w] + d[i][w - coins[i]]
        
        if amount == 0:
            return 1
        elif len(coins) == 0:
            return 0
        
        
        d = [[0 for _ in range(amount+1)] for __ in range(len(coins))]
        
        # Base: 
        for i in range(len(coins)):
            d[i][0] = 1
        
        for i in range(len(coins)):
            for w in range(1, amount+1):
                if w - coins[i] >=0:
                    d[i][w] = d[i-1][w] + d[i][w - coins[i]]
                else:
                    d[i][w] = d[i-1][w]
      
        # print(d)
        return d[-1][-1]