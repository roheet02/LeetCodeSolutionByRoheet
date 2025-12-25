#Maximize Happiness of Selected Children

class Solution:
    def maximizeHappinesOfChildren(self,happiness,k):
        happiness.sort(reverse=True)
        total=0
        for i in range(k):
            total+=max(happiness[i]-i,0)
        return total
print(Solution().maximizeHappinesOfChildren([1,2,3],2))
print(Solution().maximizeHappinesOfChildren([2,3,4,5], 1))