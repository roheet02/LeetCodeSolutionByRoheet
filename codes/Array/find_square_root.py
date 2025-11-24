## This is using Newton’s Method Formula   which is x(n+1)=(xn+S/xn)/2

class Solution1:
    def squareRoot(self,x:int):
        if x==0:
            return 0
        r=x
        while r*r>x:
            r=(r+(x//r))//2
        return r

result=Solution1().squareRoot(144)
print(result)


# #general method
# 🚀 Binary Search in One Sentence
# Binary search repeatedly checks the middle of a sorted range and eliminates half of the values each time.

class Solution2:
    def squareRoot(self,x:int):
        if x<2:
            return x
        left ,right = 1, x//2
        while left<=right:
            mid = (left+right)//2
            sqrt=mid*mid
            if sqrt==x:
                return mid
            elif sqrt<x:
                left =mid+1
            else :
                right =mid-1
        return right


result=Solution2().squareRoot(144)
print(result)


