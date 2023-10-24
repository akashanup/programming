class Solution:
    def nextGreaterElements(self, nums: List[int]) -> List[int]:
        n = len(nums)
        result = [-1] * n
        stack = []

        """
        This question is very similar to Next Greater Element I.
        The only difference here is that the array is circular.
        So to handle circular array, we will visualize it as a duplicate array is pasted after the original array.
        Hence now the length becomes 2*n so the iteration will start from 2n-1 till 0.
        Now we will be storing answers in results only when i < n and take care of other imaginary values by using modulo operator.
        """

        # Finding next greater element for all elements nums and storing in lookup.
        for i in range((2 * n) - 1, -1, -1):
            while stack and nums[i % n] >= stack[-1]:
                stack.pop()
            if i < n:
                result[i] = stack[-1] if stack else -1
            stack.append(nums[i % n])

        return result
