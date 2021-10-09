class Solution:
    def heapify(self, nums, n, i):
        """
            Since max heap is a complete binary tree and it can be implemented using array.
            If i is a parent node then,
                left child would be 2*i + 1
                right child would be 2*i + 2
        """
        largest = i
        l = 2*i + 1
        r = 2*i + 2

        # Check if left child exists and value of root is smaller than left child
        if l < n and nums[largest] < nums[l]:
            largest = l

        # Check if right child exists and value of root is smaller than right child
        if r < n and nums[largest] < nums[r]:
            largest = r

        # Check if root needs to be modified
        if largest != i:
            # Swap
            nums[largest], nums[i] = nums[i], nums[largest]
            self.heapify(nums, n, largest)

    def sortArray(self, nums: List[int]) -> List[int]:
        n = len(nums)

        # Build maxheap
        for i in range((n // 2) -1, -1, -1):
            self.heapify(nums, n, i)

        # Exract element one by one
        for i in range(n-1, 0, -1):
            nums[0], nums[i] = nums[i], nums[0]
            self.heapify(nums, i, 0)

        return nums
