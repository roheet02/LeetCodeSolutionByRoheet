# Two Best Non-Overlapping Events
from collections import deque
from operator import itemgetter
class Solution:
    def maxTwoEvents(self, events):

        end_sorted = deque(sorted(events, key=itemgetter(1)))
        start_sorted = sorted(events, key=itemgetter(0))

        ans = max(v for _, _, v in events)

        end_max = 0  

        for start, end, value in start_sorted:
            while end_sorted and end_sorted[0][1] < start:
                _, _, v = end_sorted.popleft()
                end_max = max(end_max, v)
            ans = max(ans, value + end_max)

        return ans

print(Solution().maxTwoEvents([[1,3,2],[4,5,2],[1,5,5]]))