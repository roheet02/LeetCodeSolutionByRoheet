class Solution:
    def numOfWays(self, n):
        MOD = 10**9 + 7
        # Base case
        a, b = 6, 6   # a = type A, b = type B
        for _ in range(2, n + 1):
            new_a = (2 * a + 2 * b) % MOD
            new_b = (2 * a + 3 * b) % MOD
            a, b = new_a, new_b
        return (a + b) % MOD

print(Solution().numOfWays(1))
