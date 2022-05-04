class Solution:
    def maxOperations(self, nums: List[int], k: int) -> int:
        operations = 0
        hashmap = {}
        for num in nums:
            counterPart = k - num
            if counterPart in hashmap and hashmap[counterPart] > 0:
                operations += 1
                hashmap[counterPart] -= 1
            else:
                if num in hashmap:
                    hashmap[num] += 1
                else:
                    hashmap[num] = 1
        return operations
