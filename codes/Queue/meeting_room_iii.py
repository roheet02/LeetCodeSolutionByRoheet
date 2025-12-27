##meeting rooms iii
class Solution:
    def mostBooked(self, n, meetings):
        meetings.sort()
        count=[0]*n
        timer=[0]*n
        itr=0
        while itr<len(meetings):
            start, end =meetings[itr]
            dur =end-start
            room=-1
            earliest=float('inf')
            earliesrRoom=-1
            for i in range(n):
                if timer[i]<earliest:
                    earliest=timer[i]
                    earliestRoom=i
                if timer[i]<=start:
                    room =i
                    break
            if room !=-1:
                timer[room]=end
                count[room]+=1
            else:
                timer[earliestRoom]+=dur
                count[earliestRoom]+=1
            itr+=1
        maxv=0
        idx=0
        for i in range(n):
            if count[i]>maxv:
                maxv=count[i]
                idx=i
        return idx        
print(Solution().mostBooked(2,[[0,10],[1,5],[2,7],[3,4]]))
print(Solution().mostBooked(3,[[1,20],[2,10],[3,5],[4,9],[6,8]]))