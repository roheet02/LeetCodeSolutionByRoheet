#Product of Array Except Self

class Solution:
    def productExceptSelf(self, nums):
        n=len(nums)
        answer=[1]*n
        prefix=1
        for i in range(n):
            answer[i]=prefix
            prefix*=nums[i]
            print(prefix)
            print(answer)
        print(answer)
        rightProduct=1
        for i in range(n-1,-1,-1):
            answer[i] *= rightProduct
            rightProduct *= nums[i]
            print(rightProduct)
            print(answer)
        return answer
print(Solution().productExceptSelf([1,2,3,4]))