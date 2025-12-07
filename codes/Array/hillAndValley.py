#Count Hills and Valleys in an Array
#You are given a 0-indexed integer array nums. An index i is part of a hill in nums
# if the closest non-equal neighbors of i are smaller than nums[i]. Similarly, an index i is part of a valley 
# in nums if the closest non-equal neighbors of i are larger than nums[i]. Adjacent indices i and j are part 
# of the same hill or valley if nums[i] == nums[j].

class Solution:
    def countHillValley(self, nums):
        arr =[nums[0]]
        for i in range(1,len(nums)):
            if nums[i]!=nums[i-1]:
                arr.append(nums[i])
        count=0
        for i in range(1, len(arr) - 1):
            if arr[i-1]>arr[i] and arr[i]<arr[i+1]:
                count+=1 #valley
            if arr[i-1]<arr[i] and arr[i]>arr[i+1]:
                count +=1 #hills
        return count
            



print(Solution().countHillValley([2,4,5,3,6,7,2,7]))