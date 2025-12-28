# Count Negative Numbers in a Sorted Matrix 
class Solution:
    def countNegatives(self, grid):
        count=0
        for i in grid:
            for j in i:
                if j<0:
                    count+=1
        return count

print(Solution().countNegatives([[4,3,2,-1],[3,2,1,-1],[1,1,-1,-2],[-1,-1,-2,-3]]))
print(Solution().countNegatives([[3,2],[1,0]]))

