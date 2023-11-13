"""
A naive way to do this is to form all the possible subarrays and add the minimum of each subarray.
This would definitely give O(N^2) TC.
Another approach could be, if we find out the contribution of each array element in the subarrays, we can get the sum.

Find the nearest smaller element than the current element in both left and right sides, to get a window where the
current element is the minimum element in all the subarrays formed in that particular window.
For example, for array [5, 4, 2, 3, 1], we want to find the contribution of element 2-
The contribution of 2 in the subarrays formed on the left side is [2], [4, 2] and [5, 4, 2]
The contribution of 2 in the subarrays formed on the right side is [2] and [2, 3].
So for an element, if we find the length of array on the left (let us say x) and the length of array on the right
(let us say y) for potential subarrays so total length is (x+y-1), and we know that for an array of length n, the total
number of subarrays are (n*(n+1)/2), we can find the total number of subarrays where the element is minimum and that is-
((x+y-1)*(x+y)/2) - ((x-1)*(x)/2) - ((y-1)*y/2) => x*y
Note:
    1. We have negated ((x-1)*(x)/2) because of the subarrays which are formed by elements on the left only.
        For example, subarrays formed by [5, 4]
    2. We have negated ((y-1)*(y)/2) because of the subarrays which are formed by elements on the right only.
        For example, subarrays formed by [3]
So the total contribution of 2 is, 2*(x*y). Here x is 3 and y is 2. So, 2*3*2 => 12.
Verification for the above array - Subarrays where 2 is a minimum element =>
[5, 4, 2, 3], [5, 4, 2], [4, 2, 3], [4, 2], [2], [2,3]
"""


class Solution:
    def previousSmallerElementIndex(self, arr):
        smallerElementIndex = [-1] * len(arr)
        stack = []
        for i in range(len(arr)):
            while stack and arr[i] <= arr[stack[-1]]:
                stack.pop()
            if stack:
                smallerElementIndex[i] = stack[-1]
            stack.append(i)
        return smallerElementIndex

    def nextSmallerElementIndex(self, arr):
        smallerElementIndex = [-1] * len(arr)
        stack = []
        for i in range(len(arr)-1, -1, -1):
            while stack and arr[i] < arr[stack[-1]]:
                stack.pop()
            if stack:
                smallerElementIndex[i] = stack[-1]
            stack.append(i)
        return smallerElementIndex

    def sumSubarrayMins(self, arr: List[int]) -> int:
        nextIdx = self.nextSmallerElementIndex(arr)
        previousIdx = self.previousSmallerElementIndex(arr)
        result = 0
        for i in range(len(arr)):
            x = i-previousIdx[i]
            if nextIdx[i] == -1:
                y = len(arr)-i
            else:
                y = nextIdx[i]-i
            contribution = arr[i]*x*y
            result += contribution
        return result % ((10**9)+7)