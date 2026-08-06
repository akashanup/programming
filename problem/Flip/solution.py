class Solution:
    def flip(self, A):
        """
        We need to find the longest subarray in which the count of 0s is greater than the count of 1s.
        If we convert 1 to -1 and 0 to 1, then we need to find the subarray with a maximum sum.
        We can use Kadane's algorithm for this.
        """
        lookup = {
            "0": 1,
            "1": -1
        }
        maxSum = 0
        currSum = 0
        start, end = 0, 0
        ans = [start, end]
        for i, ch in enumerate(A):
            currSum += lookup[ch]
            if currSum > maxSum:
                # Found new potential answer
                maxSum = currSum
                end = i
                ans = [start, end]
            if currSum < 0:
                currSum = 0
                # look for the next subarray
                start = i+1
        return ans


print(Solution().flip("010"))
print(Solution().flip("011"))
print(Solution().flip("110010011"))
print(Solution().flip("1101010001"))
