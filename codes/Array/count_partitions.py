##Count Partitions With Max-Min Difference at Most K
from collections import deque

class Solution:
    def countPartitions(self, nums, k):
        N = len(nums)
        MOD = 10**9 + 7
        dp = [1] + [0] * (N)
        acc = 1
        minq = deque()
        maxq = deque()
        i = 0
        for j in range(N):
            while maxq and nums[j] > nums[maxq[-1]]:
                maxq.pop()
            maxq.append(j)

            while minq and nums[j] < nums[minq[-1]]:
                minq.pop()
            minq.append(j)

            while nums[maxq[0]] - nums[minq[0]] > k:
                acc = (acc - dp[i]) % MOD
                i += 1
                if minq[0] < i:
                    minq.popleft()
                if maxq[0] < i:
                    maxq.popleft()
            dp[j+1] = acc
            acc = (acc + dp[j+1]) % MOD
        return dp[N]

print(Solution().countPartitions([9,4,1,3,7],4))