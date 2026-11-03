class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # buy low and sell high

        min_p = prices[0]
        max_p = 0
        for p in prices[1:]:
            min_p = min(min_p, p)

            if p > min_p:
                # profit = p - min_p
                max_p = max(max_p, p - min_p)
        
        return max_p

        # min_p = 10
        # 1, min_p = 1, 
        # 0, 5 - 1
        # time complexity of o n
            

