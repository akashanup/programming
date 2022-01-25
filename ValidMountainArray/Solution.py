class Solution:
    def validMountainArray(self, arr: List[int]) -> bool:
        peak = 0
        valley = 0
        i = 1
        while i < len(arr)-1:
            # Condition to check peaks
            if arr[i-1] < arr[i] > arr[i+1]:
                peak += 1
            # Condition to check valleys
            if arr[i-1] >= arr[i] <= arr[i+1]:
                valley += 1
            i += 1
        # arr is mountain iff there is only one peak and zero valleys.
        return peak == 1 and valley == 0
