#You are given three arrays of length n that describe the properties of n coupons: code, 
# businessLine, and isActive. The ith coupon has:
#code[i]: a string representing the coupon identifier.
#businessLine[i]: a string denoting the business category of the coupon.
#isActive[i]: a boolean indicating whether the coupon is currently active.



class Solution:  
    def validateCoupons(self, code, businessLine, isActive):

        def isValid(record):
            return (record[0] in valid_business and record[2] and record[1].replace('_', 'a').isalnum())

        valid_business = {"electronics", "grocery", "restaurant", "pharmacy"}

        ans = sorted(filter(isValid, zip(businessLine, code, isActive)))
        return [coupId for _, coupId, _ in ans]
print(Solution().validateCoupons(["SAVE20","","PHARMA5","SAVE@20"],["restaurant","grocery","pharmacy","restaurant"],[True,True,True,True]))