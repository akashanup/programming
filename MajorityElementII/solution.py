class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        """
            Let us iterate through our data and at each moment of time keep at most 2 candidates with the highest score, let us consider example 1 2 3 3 3 2 2 2 4 2.

            On first step we add 1 to our candidates, frequency 1, so we have 1: 1
            Now we add 2 to our candidates, frequency 1, so we have 1:1, 2:1.
            Now we add 3 to our candidates and we have 1:1, 2:1, 3:1. Now we subtract 1 from all frequencies, because it will not change anything.
            Now we add 3, so we have 3:1.
            Now we add 3, so we have 3:2.
            Now we add 2, so we have 3:2, 2:1.
            Now we add 2, so we have 3:2, 2:2.
            Now we add 2, so we have 3:2, 2:3.
            Now we add 4, so we have 3:2, 2:3, 4:1, subtract 1 from all, and we have 3:1, 2:2.
            Finally we add 2, so we have 3:1, 2:3.
            First stage of our algorithm is finished, we have no more than two candidates. Now we need to make sure, that these candidates indeed has frequence more than [n/3]. So we iterate through our data once again and count them. In our case 2 is true candidate and 3 need to be removed, its frequency is not big enough.
        """
        candidates = {}
        for num in nums:
            if num in candidates:
                candidates[num] += 1
            else:
                candidates[num] = 1

            if len(candidates) == 3:
                temp = {}
                for candidate, frequency in candidates.items():
                    if frequency > 1:
                        temp[candidate] = frequency-1
                candidates = temp
        output = []
        for candidate in candidates:
            count = 0
            for num in nums:
                if num == candidate:
                    count += 1
            if count > (len(nums) // 3):
                output.append(candidate)
        return output

