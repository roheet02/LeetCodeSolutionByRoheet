#N-Repeated Element in Size 2N Array

from typing import List

class Solution:
    def repeatedNTimes(self, nums):
        freq = {}

        for num in nums:
            if num in freq:
                return num   # repeated element found
            freq[num] = 1

print(Solution().repeatedNTimes([2,1,2,5,3,2]))