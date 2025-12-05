class Solution:
    def countPartition(self,nums):
        total=sum(nums)
        n=len(nums)
        if total%2==0:
            return n-1
        else:
            return 0

print(Solution().countPartition([2,4,6,8]))