# longest substring usnig sliding window

class Solution:
    def longestSubstring(self, s:str):
        stack=set()
        left=0
        max_len=0
        for right in range(len(s)):
            while s[right] in stack:
                stack.remove(s[left])
                left+=1
            stack.add(s[right])
            max_len=max(max_len,right-left+1)
        return max_len

print(Solution().longestSubstring("ahidhshuc"))
# print(Solution().longestSubstring("rohit"))