class Solution():
    def longestPrefix(self,strs):
        if not strs:
            return ""
        prefix = strs[0]

        for i in strs[1:]:
            while not i.startswith(prefix):
                prefix=prefix[:-1]
                if not prefix:
                    return ""
        return prefix
    
strs=["flower","flow","flo"]
print(Solution().longestPrefix(strs))