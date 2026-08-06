class OrderedStream:

    def __init__(self, n: int):
        self.seen = {}
        self.ptr = 1

    def insert(self, keyId: int, value: str) -> List[str]:
        seen, ptr = self.seen, self.ptr

        seen[keyId] = value
        result = []
        while ptr in seen:
            result.append(seen[ptr])
            # Below line is optional
            del seen[ptr]
            ptr += 1

        self.ptr = ptr
        return result


# Your OrderedStream object will be instantiated and called as such:
# obj = OrderedStream(n)
# param_1 = obj.insert(idKey,value)
