#. Count Square Sum Triples
#A square triple (a,b,c) is a triple where a, b, and c are integers and a2 + b2 = c2.
#Given an integer n, return the number of square triples such that 1 <= a, b, c <= n.

class Solution:
    def countTriples(self,n):
        squares = {i*i:i for i in range(1,n+1)}
        count=0
        for a in range(1,n+1):
            a2=a*a
            for b in range(1,n+1):
                c2=a2+b*b
                if c2 in squares:
                    c=squares[c2]
                    if c<=n:
                        count+=1
        return count

print(Solution().countTriples(100))