#Delete Columns to Make Sorted

class Solution():
    def minDeletionSize(self,strs):
        deletions=0
        rows=len(strs)
        cols=len(strs[0])
        for i in range(cols):
            for j in range(rows-1):
                if strs[j][i]>strs[j+1][i]:
                    deletions+=1
                    break
        return deletions

print(Solution().minDeletionSize(["cba","daf","ghi"]))