# ## Merge two list 
class Solution1:
    def mergeTwoList(self,nums1,m,nums2,n):

        temp=nums1[:m]+nums2[:n]
        temp.sort()
        for i in range(len(temp)):
            nums1[i]=temp[i]
        return nums1
              
print(Solution1().mergeTwoList([1,2,3,0,0,0], 3, [7,8,9], 3))


class Solution2:
    def mergeTwoList(self, nums1, m, nums2, n):
        i = m - 1   # pointer for nums1
        j = n - 1   # pointer for nums2
        k = m + n - 1  # pointer for final position in nums1

        while i >= 0 and j >= 0:
            if nums1[i] > nums2[j]:
                nums1[k] = nums1[i]
                i -= 1
            else:
                nums1[k] = nums2[j]
                j -= 1
            k -= 1

        while j >= 0:   # Only copy remaining nums2
            nums1[k] = nums2[j]
            j -= 1
            k -= 1
        return nums1


print(Solution2().mergeTwoList([1,2,3,0,0,0], 3, [7,8,9], 3))