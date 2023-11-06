"""
Start checking from 0th gas station to travel the farthest gas station.

If the car can't reach at any of the gas stations (let's say jth gas station) then calculate the amount of
deficitGas which if would be there, then the car would have travelled to jth station. **This also tells the extra amount
of gas required to travel to jth station from the current station**

Now start from jth station and travel to the farthest station and repeat the above step.

Once all the stations have been traveled, check whether the current balance >= deficit.
If yes, then the last station would be the answer
Else -1

"""


class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        balanceGas = 0
        deficitGas = 0
        startStation = 0
        i = 0
        while i < len(gas):
            balanceGas += gas[i] - cost[i]
            if balanceGas < 0:
                deficitGas += balanceGas
                balanceGas = 0
                startStation = i
            i += 1
        if balanceGas + deficitGas >= 0:
            return startStation
        else:
            return -1
