class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        n = len(nums)
        lookup = {}
        for i in range(2**n):
            binI = bin(i)[2:]
            binI = ('0' * (n - len(binI))) + str(binI)
            temp = []
            for j in range(n):
                if binI[j] == '1':
                    temp.append(nums[j])
            lookup[tuple(sorted(temp))] = True

        return [list(i) for i in lookup.keys()]
