class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        if sum(gas) < sum(cost):
            return -1
        start, end = 0, len(gas)-1
        total_gas = gas[end] - cost[end]
        while start < end:
            if total_gas < 0:
                end -= 1
                total_gas += gas[end]-cost[end]
            else:
                total_gas += gas[start] - cost[start] 
                start += 1
        return end