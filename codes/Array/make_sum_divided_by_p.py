#we used sliding window and hashmapping to solve the solution
class Solution:
    def minSubarray(self, nums, p) :
        total =sum(nums)
        target=total%p
        if target ==0:
            return 0
        
        prefix =0
        hashmap = {0:-1}
        result=len(nums)

        for i,num in enumerate(nums):
            prefix=(prefix+num)%p
            needed =(prefix-target)%p

            if needed in hashmap :
                result = min(result,i-hashmap[needed])
            hashmap[prefix]=i

        return result if result<len(nums) else -1

print(Solution().minSubarray([2,3,4,1],6))


        