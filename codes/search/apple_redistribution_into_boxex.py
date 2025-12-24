#Apple Redistribution into Boxes
class Solution:
    def minimumBoxes(self, apple, capacity):
        #calculate the total number of apples from all piles
        total_apples = sum(apple)
        #sort the box capacities in descending order
        #so we use the largest boxes first
        capacity.sort(reverse=True)
        #this variable counts how many boxes we have used
        need = 0
        #keep using boxes until all apples are placed
        while total_apples > 0:
            #use the next largest box and reduce the remaining apples
            total_apples -= capacity[need]
        #increment the number of boxes used
            need += 1
        #return the minimum number of boxes required
        return need

print(Solution().minimumBoxes([1,3,2],[4,3,1,5,2]))