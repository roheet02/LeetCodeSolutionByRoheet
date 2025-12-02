class Solution:
    def countTrapezoids(self, points):
        ys={}
        ans=0
        for x,y in points:
            if y in ys:
                ys[y]+=1
            else:
                ys[y]=1
            
        ls = list(ys.values())
        MOD = 1000000007
        summ=0
        for i in range(len(ls)):
            n=ls[i]*(ls[i]-1)//2
            ans=(ans+(n+summ))%MOD
            summ=(summ+n)%MOD
        ans=int(ans)
        return ans
    
print(Solution().countTrapezoids([[1,0], [2,0], [3,0], [2,2], [3,2]]))