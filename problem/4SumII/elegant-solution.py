class Solution:
    def fourSumCount(self, nums1: List[int], nums2: List[int], nums3: List[int], nums4: List[int]) -> int:
        hashmap1_2 = {}
        for num1 in nums1:
            for num2 in nums2:
                sum1_2 = num1+num2
                if sum1_2 in hashmap1_2:
                    hashmap1_2[sum1_2] += 1
                else:
                    hashmap1_2[sum1_2] = 1

        result = 0
        for num3 in nums3:
            for num4 in nums4:
                _4SumCounterPart = 0 - (num3+num4)
                if _4SumCounterPart in hashmap1_2:
                    result += hashmap1_2[_4SumCounterPart]
        return result
