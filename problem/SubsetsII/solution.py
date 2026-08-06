class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        n = len(nums)
        lookup = {}
        '''
            Since the total number of subsets that can be formed from a n length list is 2^n.
            So convert each number from 0 to n and convert it to its binary form of n bits.
            Now, iterate over each bit of binary form and if its 1 then add nums of that index to current subset.
        '''
        for i in range(2**n):
            binI = bin(i)[2:]
            binI = ('0' * (n - len(binI))) + str(binI)
            temp = []
            for j in range(n):
                if binI[j] == '1':
                    temp.append(nums[j])
            lookup[tuple(sorted(temp))] = True

        return [list(i) for i in lookup.keys()]
