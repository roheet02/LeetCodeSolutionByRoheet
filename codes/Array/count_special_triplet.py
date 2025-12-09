#Count Special Triplets
#You are given an integer array nums.
#A special triplet is defined as a triplet of indices (i, j, k) such that:
#0 <= i < j < k < n, where n = nums.length
#nums[i] == nums[j] * 2
#nums[k] == nums[j] * 2

class Solution:
    def specialTriplet(self,nums):
        mod = 10**9+7
        from collections import Counter
        rightCount=Counter(nums)
        leftCount=Counter()
        c=0
        for j,val in enumerate(nums):
            rightCount[val]-=1
            target=2*val
            c=(c+leftCount[target]*rightCount[target])%mod
            leftCount[val]+=1
        return c

print(Solution().specialTriplet([8,4,2,8,4]))