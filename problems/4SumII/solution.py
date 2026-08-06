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

        hashmap3_4 = {}
        for num3 in nums3:
            for num4 in nums4:
                sum3_4 = num3+num4
                if sum3_4 in hashmap3_4:
                    hashmap3_4[sum3_4] += 1
                else:
                    hashmap3_4[sum3_4] = 1

        nums1_2 = sorted(list(hashmap1_2.keys()))
        nums3_4 = sorted(list(hashmap3_4.keys()))

        result = 0
        n1_2 = 0
        n3_4 = len(nums3_4) - 1
        while n1_2 < len(nums1_2) and n3_4 >= 0:
            _4Sum = nums1_2[n1_2] + nums3_4[n3_4]
            if _4Sum > 0:
                n3_4 -= 1
            elif _4Sum < 0:
                n1_2 += 1
            else:
                result += (hashmap1_2[nums1_2[n1_2]] * hashmap3_4[nums3_4[n3_4]])
                n1_2 += 1
                n3_4 -= 1
        return result
