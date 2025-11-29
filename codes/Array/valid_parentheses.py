class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        pairs = {')': '(', '}': '{', ']': '['}
        for char in s:
            # If it's an opening bracket, push to stack
            if char in pairs.values():
                stack.append(char)
            # If it's a closing bracket
            elif char in pairs:
                # Stack must not be empty and must match the correct opening bracket
                if not stack or stack[-1] != pairs[char]:
                    return False
                stack.pop()
            else:
                # Invalid character (not required for this problem)
                return False
        # Stack must be empty for the string to be valid
        return len(stack) == 0

print(Solution().isValid("{}[]()"))