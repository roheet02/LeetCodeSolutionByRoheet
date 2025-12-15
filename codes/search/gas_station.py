#gas station
class Solution:
    def canCompleteCircuit(self,gas,cost):
        total_gas=0
        tank=0
        start=0
        for i in range(len(gas)):
            diff=gas[i]-cost[i]
            total_gas+=diff
            tank+=diff

            if tank<0:
                start =i+1
                tank=0
        return start if total_gas>=0 else -1

print(Solution().canCompleteCircuit([1,2,3,4,5],[3,4,5,1,2]))

#Solution2
class Solution:
    def canCompleteCircuit(self,gas,cost):
        if sum(gas)<sum(cost):
            return -1

        n=len(gas)
        running_gas_balance=0
        lowest_gas=0
        index_lowest_gas=float("inf")
        for i in range(n):
            running_gas_balance+=gas[i]-cost[i]
            if running_gas_balance<lowest_gas:
                lowest_gas=running_gas_balance
                index_lowest_gas=i

        return (index_lowest_gas+1)%n
print(Solution().canCompleteCircuit([1,2,3,4,5],[3,4,5,1,2]))
