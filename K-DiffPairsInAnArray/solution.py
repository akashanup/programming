class Solution:
    def addPair(self, hashmap, pairs, num, counterPart):
        if counterPart in hashmap and (counterPart != num or (counterPart == num and hashmap[num] > 1)):
            pairs.add((num, counterPart) if num < counterPart else (counterPart, num))
        # if counterPart in hashmap:
        #     if counterPart == num:
        #         if hashmap[num] > 1:
        #             pairs.add((num, num))
        #     else:
        #         pairs.add((num, counterPart) if num < counterPart else (counterPart, num))


    def findPairs(self, nums: List[int], k: int) -> int:
        hashmap = {}
        for num in nums:
            if num in hashmap:
                hashmap[num] += 1
            else:
                hashmap[num] = 1

        pairs = set()
        for num in hashmap.keys():
            # counterPart1 = k - num
            # counterPart2 = -k - num
            self.addPair(hashmap, pairs, num,  k + num)
            self.addPair(hashmap, pairs, num, -k + num)
        return len(pairs)
