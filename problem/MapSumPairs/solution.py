class MapSum:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.pair = {}

    def insert(self, key: str, val: int) -> None:
        self.pair[key] = val

    def sum(self, prefix: str) -> int:
        pairSum = 0
        for key in self.pair:
            if key.startswith(prefix):
                pairSum += self.pair[key]
        return pairSum
