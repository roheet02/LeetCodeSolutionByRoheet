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
