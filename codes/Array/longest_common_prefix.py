class Solution():
    def longestPrefix(self,strs):
        if not strs:
            return ""
        prefix = strs[0] #will select the first element

        for i in strs[1:]:
            while not i.startswith(prefix):  #i.startswith will check whether i and prefix is matching or not
                prefix=prefix[:-1]  # this will start shrinking of the string
                if not prefix:
                    return ""
        return prefix
    
strs=["flower","flow","flo"]
print(Solution().longestPrefix(strs))