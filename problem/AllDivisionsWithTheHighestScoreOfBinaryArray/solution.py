class Solution:
    def maxScoreIndices(self, nums: List[int]) -> List[int]:
        n = len(nums)
        ones = sum(nums)
        if n == ones:
            return [0]
        zeros = n - ones
        if n == zeros:
            return [n]
        tempZeros = 0
        tempOnes = ones
        # If partitioned at 0th index
        result = [0]
        i = 0
        divisionScore = ones
        while i < n:
            if nums[i] == 0:
                tempZeros += 1
            else:
                tempOnes -= 1
            if tempZeros + tempOnes > divisionScore:
                result = [i+1]
                divisionScore = tempZeros + tempOnes
            elif tempZeros + tempOnes == divisionScore:
                result.append(i+1)
            i += 1
        return result
