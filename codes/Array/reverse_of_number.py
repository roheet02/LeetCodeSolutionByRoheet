class Solution:
    def reverseNumber(self,x):
        numm=0
        sign=1 if x>0 else -1   # keeping sign separate
        x=abs(x)
        while x!=0:
            last_num = x%10 #get last number of numbes
            x//=10          #delete last number
            if numm>214748364 or (numm==214748364 and last_num >7):  #make sure that it wont get overflow after 32 bit
                return 0
            numm=numm*10+last_num  # here we are reversing the number keep storing it 

        return numm*sign

print(Solution().reverseNumber(12349793))


#solution2 more optimise

class Solution:
    def reverseNumber(self, x: int) -> int:
        x1 = str(abs(x))
        x2 = x1[::-1]
        res = int(x2)
        if x < 0:
            res = -res
        if res < -(2**31) or res > 2**31 - 1:
            return 0
        return res

print(Solution().reverseNumber(12349793))
