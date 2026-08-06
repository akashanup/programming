class Solution:
    def slowestKey(self, releaseTimes: List[int], keysPressed: str) -> str:
        maxTime, key = releaseTimes[0], keysPressed[0]
        for i in range(1, len(releaseTimes)):
            if releaseTimes[i] - releaseTimes[i-1] > maxTime:
                maxTime = releaseTimes[i] - releaseTimes[i-1]
                key = keysPressed[i]
            elif releaseTimes[i] - releaseTimes[i-1] == maxTime:
                key = key if key >= keysPressed[i] else keysPressed[i]
        return key
