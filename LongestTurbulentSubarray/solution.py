class Solution:
    def maxTurbulenceSize(self, arr: List[int]) -> int:
        if len(arr) == 1:
            return 1
        even, odd = 0, 0
        maxSize = 0
        for k in range(len(arr) - 1):
            if k % 2:
                # Odd index
                if arr[k] < arr[k + 1]:
                    even += 1
                    maxSize = max(maxSize, odd)
                    odd = 0
                elif arr[k] > arr[k + 1]:
                    maxSize = max(maxSize, even)
                    even = 0
                    odd += 1
                else:
                    maxSize = max(maxSize, even, odd)
                    odd = 0
                    even = 0
            else:
                # Even index
                if arr[k] > arr[k + 1]:
                    maxSize = max(maxSize, odd)
                    odd = 0
                    even += 1
                elif arr[k] < arr[k + 1]:
                    # odd = odd + 1 if odd > 0 else 0
                    odd += 1
                    maxSize = max(maxSize, even)
                    even = 0
                else:
                    maxSize = max(maxSize, even, odd)
                    even = 0
                    odd = 0
        maxSize = max(maxSize, even, odd)
        return maxSize + 1
