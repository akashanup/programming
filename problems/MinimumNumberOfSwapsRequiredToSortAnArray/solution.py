class Solution:
    def minSwaps(self, arr):
        arrLen = len(arr)
        lookup = {}
        for i in range(arrLen):
            lookup[arr[i]] = i
        sortedArr = sorted([_ for _ in arr])
        swaps = 0
        for i in range(arrLen):
            if arr[i] != sortedArr[i]:
                swaps += 1
                temp = arr[i]
                # Swap the current element with the right index so that arr[0] to arr[i] is sorted
                arr[i], arr[lookup[sortedArr[i]]] = arr[lookup[sortedArr[i]]], arr[i]
                # Update the indexes in the hashmap accordingly
                lookup[temp] = lookup[sortedArr[i]]
                lookup[sortedArr[i]] = i
        return swaps


'''
    Time Complexity: O(n*log(n)) taken by sorting.
'''
