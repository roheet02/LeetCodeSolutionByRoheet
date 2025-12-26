#word_pattern
class Solution:
    def wordPattern(self, pattern, s):
        words=s.split(" ")
        if len(pattern) != len(words):
            return False
        return len(set(pattern))==len(set(words)) == len(set(zip(pattern,words)))
print(Solution().wordPattern("abba","dog cat cat dog"))
print(Solution().wordPattern("abba","dog cat cat fish"))

    

