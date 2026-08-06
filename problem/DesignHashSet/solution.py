class MyHashSet:

    def __init__(self):
        self.size = 1000
        self.ranges = [[] for _ in range(self.size)]

    def getHash(self, key):
        return key % self.size
        
    def getLocation(self, key):
        rangeIdx = self.getHash(key)
        for index, val in enumerate(self.ranges[rangeIdx]):
            if key == val:
                return rangeIdx, index
        return rangeIdx, None
        
    def add(self, key: int) -> None:
        rangeIdx, keyIdx = self.getLocation(key)
        if keyIdx is None:
            self.ranges[rangeIdx].append(key)

    def remove(self, key: int) -> None:
        rangeIdx, keyIdx = self.getLocation(key)
        if keyIdx is not None:
            # Move the key to end and pop
            self.ranges[rangeIdx][keyIdx],self.ranges[rangeIdx][-1] = self.ranges[rangeIdx][-1], self.ranges[rangeIdx][keyIdx]
            self.ranges[rangeIdx].pop()

    def contains(self, key: int) -> bool:
        rangeIdx, keyIdx = self.getLocation(key)
        return keyIdx is not None


# Your MyHashSet object will be instantiated and called as such:
# obj = MyHashSet()
# obj.add(key)
# obj.remove(key)
# param_3 = obj.contains(key)
