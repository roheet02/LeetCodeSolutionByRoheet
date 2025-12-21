class Solution:
    def minDeletionSize(self, strs):
        # Number of strings (rows)
        n = len(strs)
        # Length of each string (number of columns)
        m = len(strs[0])
        # resolved[i] is True if the order between strs[i] and strs[i+1]
        # is already confirmed to be strictly increasing
        resolved = [False] * (n - 1)
        # Count of adjacent string pairs whose order is not yet resolved
        unresolved = n - 1
        # Number of columns that must be deleted
        deletions = 0
        # Iterate through each column from left to right
        for col in range(m):
            # If all pairs are resolved, we can stop early
            if unresolved == 0:
                break
            bad = False  # Indicates whether this column breaks sorting
            # Check if this column violates lexicographical order
            for i in range(n - 1):
                # Only check pairs that are not already resolved
                if not resolved[i] and strs[i][col] > strs[i + 1][col]:
                    bad = True
                    break
            # If this column causes a violation, delete it
            if bad:
                deletions += 1
                continue
            # Otherwise, update resolved pairs where order is determined
            for i in range(n - 1):
                if not resolved[i] and strs[i][col] < strs[i + 1][col]:
                    resolved[i] = True
                    unresolved -= 1
        # Return the total number of deleted columns
        return deletions
# Example test cases
print(Solution().minDeletionSize(["ca","bb","ac"]))
# print(Solution().minDeletionSize(["xc","yb","za"]))
