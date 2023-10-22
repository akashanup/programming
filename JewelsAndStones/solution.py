class Solution:
    def numJewelsInStones(self, jewels: str, stones: str) -> int:
        hashmap = {}
        for ch in stones:
            if ch not in hashmap:
                hashmap[ch] = 0
            hashmap[ch] += 1

        result = 0
        for ch in jewels:
            if ch in hashmap:
                result += hashmap[ch]

        return result
