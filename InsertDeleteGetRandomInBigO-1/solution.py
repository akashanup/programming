from random import random


class RandomizedSet:

    def __init__(self):
        self.hash = {}
        self.data = []

    def insert(self, val: int) -> bool:
        if val in self.hash:
            return False
        self.hash[val] = len(self.data)
        self.data.append(val)
        return True

    def remove(self, val: int) -> bool:
        if val in self.hash:
            # Shift the element that needs to be deleted to right end and just pop. This will be much more efficient then traditional pop based on the index.
            lastHashIndex = self.data[-1]
            index = self.hash[val]
            self.hash[lastHashIndex] = index
            self.data[-1], self.data[index] = self.data[index], self.data[-1]
            self.data.pop()
            self.hash.pop(val)
            return True
        return False

    def getRandom(self) -> int:
        return random.choice(self.data)


# Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()
