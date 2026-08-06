class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:
        max1s = 0
        n = len(nums)
        if k == 0:
            count = 0
            for i in range(n):
                if nums[i] == 0:
                    count = 0
                else:
                    count += 1
                max1s = max(max1s, count)
        else:
            end = 0
            flipped = 0
            start = 0
            while end < n:
                # If the number is 1 or the we can flip the number from 0 to 1 then add 1 to the flipped and move to next index.
                if 0 <= flipped < k or nums[end] == 1:
                    if nums[end] == 0:
                        flipped += 1
                    if end == n - 1:
                        max1s = max(max1s, end - start + 1)
                    end += 1
                else:
                    max1s = max(max1s, end - start)
                    # Change window position.
                    # If starting position is 0 then move the window to unit distance from left.
                    # Else move the window to skip the first set of subsequent ones and a subsequent 0 to start for a new sequence.
                    # Since we have skipped a 0 also so 1 will be subtracted from the flipped.
                    if nums[start] == 0:
                        start += 1
                    else:
                        while nums[start] == 1:
                            start += 1
                        start += 1
                    flipped -= 1
        return max1s
