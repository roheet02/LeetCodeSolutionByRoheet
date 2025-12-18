#Best Time to Buy and Sell Stock using Strategy
class Solution:
    def maxProfit(self, prices, strategy, k: int):
        n=len(prices)
        base=sum(prices[i]*strategy[i] for i in range(n))
        pref_orig=[0]*(n+1)
        pref_price=[0] * (n + 1)
        for i in range(n):
            pref_orig[i+1]=pref_orig[i]+strategy[i]*prices[i]
            pref_price[i+1]=pref_price[i]+prices[i]
        ans=base
        half=k//2
        for l in range(n-k+1):
            mid=l+half
            r=l+k
            left_loss = pref_orig[mid] - pref_orig[l]
            # right half gain
            right_gain = (pref_price[r] - pref_price[mid]) - (pref_orig[r] - pref_orig[mid])

            delta = -left_loss + right_gain
            ans = max(ans, base + delta)   
        return ans    
print(Solution().maxProfit([4,2,8],[-1,0,1],2))