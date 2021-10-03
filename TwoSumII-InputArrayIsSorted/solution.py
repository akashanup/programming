class Solution:
    def binarySearch(self, numbers, start, end, target):
        while start <= end:
            mid = start + ((end - start) // 2)
            if numbers[mid] == target:
                return mid
            elif numbers[mid] > target:
                end = mid - 1
            else:
                start = mid + 1
        return None

    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        n = len(numbers)
        for i in range(n):
            counterPartIndex = self.binarySearch(numbers, i+1, n-1, target - numbers[i])
            if counterPartIndex:
                return [i+1, counterPartIndex+1]

