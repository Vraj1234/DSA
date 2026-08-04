class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        if sum(gas) < sum(cost):
            return -1
        
        total = 0
        i = 0
        n = len(gas)
        start = -1
        while i<n:
            total += gas[i]-cost[i]

            if total <0:
                total = 0
                start = -1

            else:
                if start == -1:
                    start = i
            
            i+=1
        return start
