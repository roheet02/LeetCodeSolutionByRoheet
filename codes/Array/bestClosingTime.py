#Minimum Penalty for a Shop
class Solution:
    def bestClosingTime(self,customers):
        n=len(customers)
        penalty =customers.count("Y")
        min_penalty=penalty
        best_hour=0
        for i in range(n):
            if customers[i]=="Y":
                penalty-=1
            else:
                penalty+=1
            #to choose which time to close the shop
            if penalty<min_penalty:
                min_penalty=penalty
                best_hour=i+1
        return best_hour
print(Solution().bestClosingTime("YYNY"))
print(Solution().bestClosingTime("YYYY"))
print(Solution().bestClosingTime("NNNNN"))





