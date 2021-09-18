class Solution:
    def findOriginalArray(self, changed: List[int]) -> List[int]:
        n = len(changed)
        if n % 2:
            return []
        lookup = {}
        for num in changed:
            if num in lookup:
                lookup[num] += 1
            else:
                lookup[num] = 1
        result = []
        for num in sorted(changed):
            if lookup[num] == 0:
                continue
            if (2 * num) not in lookup or lookup[2 * num] == 0:
                return []
            result.append(num)
            lookup[num] -= 1
            lookup[2 * num] -= 1
        return result
