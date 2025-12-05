class Solution:
    def removeDuplicates(self,nums):
        if not nums:
            return 0
        k=1  #pointer to count unique numbers
        for i in range(1,len(nums)):
            if nums[i]!=nums[i-1]: #found a new unique number
                nums[k]=nums[i]
                k+=1
        return k

print(Solution().removeDuplicates([2,2,2,3,4,5,6]))