class Solution:
    def findKthPositive(self, arr: List[int], k: int) -> int:
        """
           Since the numbers are continous and array is 0-indexed array so, at any index i the arr[i] should be i+1.
           If the value at index i is not i+1 then some number(s) must be missing.
           A simple logic to calculate the count of missing numbers till index i is,
           missingNumbers = arr[i] - (i+1)
           i.e,
           missingNumbers = current value at ith index - actual value at ith index.

           Now we just need to find when the missingNumbers count becomes greater than or equal to k.
           If missingNumbers count is less than k then kth missing number would definitely lie after mid. Else, it would lie before mid.

        """
        start = 0
        end = len(arr) - 1

        while start <= end:
            mid = start + ((end - start) // 2)
            if arr[mid] - (mid+1) < k:
                start = mid + 1
            else:
                end = mid - 1
        return start + k
