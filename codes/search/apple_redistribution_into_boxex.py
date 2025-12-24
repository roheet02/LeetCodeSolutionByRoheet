#Apple Redistribution into Boxes

class Solution:
    def minimumBoxes(self,apple,capacity):
        total_apples=sum(apple)
        need =0
        capacity.sort(reverse=True)
        while total_apples>0:
            total_apples-=capacity[need]
            need+=1
        return need
print(Solution().minimumBoxes([1,3,2],[4,3,1,5,2]))