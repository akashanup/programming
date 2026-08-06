class Solution:
    def nextGreaterElement(self, n: int) -> int:
        nums = []
        while n > 0:
            nums.append(str(n%10))
            n //= 10
        nums = nums[::-1]

        i = len(nums)-2
        while i >= 0 and nums[i] >= nums[i+1]:
            i -= 1

        if i >= 0:
            j = len(nums)-1
            while j >= 0 and nums[j] <= nums[i]:
                j -= 1
            nums[i], nums[j] = nums[j], nums[i]
        else:
            return -1

        i += 1
        j = len(nums)-1
        while i < j:
            nums[i], nums[j] = nums[j], nums[i]
            i += 1
            j -= 1

        n = int(''.join(nums))
        return n if (1 <= n <= (2**31) - 1) else -1

