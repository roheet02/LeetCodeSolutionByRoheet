#Maximum Profit from Trading Stocks with Discounts
class Solution:
    def maxProfit(self, n, present, future, hierarchy, budget):
        tree = [[] for _ in range(n)]
        for u, v in hierarchy:
            tree[u - 1].append(v - 1)

        NEG = -10**15
        dp = [[[NEG] * (budget + 1) for _ in range(2)] for _ in range(n)]

        def merge(A, B):
            C = [NEG] * (budget + 1)
            for i in range(budget + 1):
                if A[i] < 0:
                    continue
                ai = A[i]
                for j in range(budget - i + 1):
                    if B[j] >= 0:
                        C[i + j] = max(C[i + j], ai + B[j])
            return C

        def dfs(u):
            for v in tree[u]:
                dfs(v)

            # merge children once
            child0 = [0] * (budget + 1)
            child1 = [0] * (budget + 1)
            for v in tree[u]:
                child0 = merge(child0, dp[v][0])
                child1 = merge(child1, dp[v][1])

            for parentBought in (0, 1):
                price = present[u] // 2 if parentBought else present[u]
                profit = future[u] - price

                # skip u
                skip = child0

                # take u
                take = [NEG] * (budget + 1)
                if price <= budget:
                    for b in range(price, budget + 1):
                        take[b] = child1[b - price] + profit

                for b in range(budget + 1):
                    dp[u][parentBought][b] = max(skip[b], take[b])

        dfs(0)
        return max(dp[0][0])

print(Solution().maxProfit(2,[1,2], [4,3],[[1,2]],3))