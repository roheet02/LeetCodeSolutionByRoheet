#Number of Ways to Divide a Long Corridor
class Solution:
    def numberOfways(self,corridor):
        mod=10**9+7
        total_c=corridor.count("S")
        if total_c ==0 or total_c%2!=0:
            return 0
        count=1
        plant_c=0
        seat_c=0
        first_section=0
        for i in corridor:
            if i =="S":
                seat_c+=1
                if seat_c ==2:
                    seat_c=0
                    if first_section:
                        count=(count*(plant_c+1))%mod
                    first_section=True
                    plant_c=0
            else:
                if first_section and seat_c==0:
                    plant_c+=1
        return count

print(Solution().numberOfways("SSPPSPS"))


