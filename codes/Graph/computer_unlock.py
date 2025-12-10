## Count the Number of Computer Unlocking Permutations
## follow j<i that is complexity[j]<complexity[i]

class Solution:
    def countPermutations(self,complexity):
        mod = 10**9+7
        if complexity[0]!=min(complexity):
            return 0
        pre_min=complexity[0]
        for i in range(1,len(complexity)):
            if pre_min>=complexity[i]:    #main condition if all this satisfly then take factorial of rest numbers
                return 0
            pre_min=min(pre_min,complexity[i])
        result=1
        for x in range(2,len(complexity)):
            result=(result*x)%mod
        return result
print(Solution().countPermutations([1,2,3,3,3]))