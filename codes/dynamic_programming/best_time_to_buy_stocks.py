#Best Time to Buy and Sell Stock V
class Solution:
    def maximumProfit(self, prices,k):
        from math import inf
        dp=[[0,-inf,-inf] for _ in range(k+1)]
        for price in prices:
            new_dp=[row[:] for row in dp]
            for t in range(k+1):
                new_dp[t][0]=max(
                    new_dp[t][0],
                    dp[t][1] + price,
                    dp[t][2] - price
                )
                if t<k:
                    new_dp[t+1][1] = max(new_dp[t+1][1], dp[t][0] - price)
                    new_dp[t+1][2] = max(new_dp[t+1][2], dp[t][0] + price)
            dp = new_dp
        return max(dp[t][0] for t in range(k + 1))  
            

print(Solution().maximumProfit([1,7,9,8,2],3))
        