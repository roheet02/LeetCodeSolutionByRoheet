class Solution:
    def countTrapezoids(self, points):
        ys = {}     # dictionary to count how many points lie on each y-level
        ans = 0

        # Count points grouped by their y-coordinate
        for x, y in points:
            if y in ys:
                ys[y] += 1
            else:
                ys[y] = 1
            
        ls = list(ys.values())  # list of counts (how many points at each y)
        MOD = 1000000007
        summ = 0                # will store running sum of C(k,2) for previous y-levels

        # Iterate through each y-level’s point count
        for i in range(len(ls)):
            # number of horizontal segments at this y-level: C(k,2)
            n = ls[i] * (ls[i] - 1) // 2

            # Add pairs: current C(k,2) with all previous C(k',2)
            # This accumulates sum_{i<j} f[i] * f[j] but using an incremental trick
            ans = (ans + (n + summ)) % MOD

            # Update running sum so next levels can multiply against it
            summ = (summ + n) % MOD

        # Convert result to integer (not necessary, but safe)
        ans = int(ans)
        return ans
    
# Test example
print(Solution().countTrapezoids([[1,0], [2,0], [3,0], [2,2], [3,2]]))
