class Solution:
    def countCollisions(self, directions: str) -> int:
        i, j = 0, len(directions)-1
        while i < len(directions) and directions[i] == 'L':
            i += 1
        
        while j >= 0 and directions[j] == "R":
            j -= 1

        print(directions[i:j+1])
        tot_count = len(directions[i:j+1])
        for char in directions[i:j+1]:
            if char == "S":
                tot_count -= 1

        return tot_count

print(Solution().countCollisions("LRRRRSS"))


class Solution:
    def countCollisions(self, directions: str) -> int:
        directions = directions.lstrip('L').rstrip('R')
        collisions = 0

        for car in directions:
            if car != 'S':
                collisions += 1
        return collisions