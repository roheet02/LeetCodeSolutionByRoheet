#Number of Smooth Descent Periods of a Stock
class Solution:
    def getDecentPeriods(self,prices):
        count=0
        temp=0
        for i in range(len(prices)):
            if i>0 and prices[i]==prices[i-1]-1:
                temp+=1    #here we are getting sequence of decent 
            else:
                temp=1
            count+=temp
        return count
print(Solution().getDecentPeriods([8,6,7,7]))