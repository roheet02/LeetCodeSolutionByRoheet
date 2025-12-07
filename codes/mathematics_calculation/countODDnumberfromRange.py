class Solution:
    def countOdds(self,low,high):
        count=0
        while low<=high:
            if low%2==1:
                count+=1
            low+=1
        return count

print(Solution().countOdds(6,8))


class Solution:
    def countOdds(self,low,high):
        return (high+1)//2-(low//2)
print(Solution().countOdds(6,15))