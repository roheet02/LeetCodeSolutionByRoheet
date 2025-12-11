class Solution:
    def countCoveredBuildings(self, n, buildings) -> int:
        from collections import defaultdict
        g1 = defaultdict(list)
        g2 = defaultdict(list)
        for x, y in buildings:
            g1[x].append(y)
            g2[y].append(x)
        for x in g1:
            g1[x].sort()
        for y in g2:
            g2[y].sort()
        ans = 0
        for x, y in buildings:
            l1 = g1[x]
            l2 = g2[y]
            if l2[0] < x < l2[-1] and l1[0] < y < l1[-1]:
                ans += 1
        return ans

print(Solution().countCoveredBuildings(3,[[1,2],[2,2],[3,2],[2,1],[2,3]]))