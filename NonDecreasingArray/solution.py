class Solution:
    def checkPossibility(self, nums: List[int]) -> bool:
        nums1 = nums[:]
        #Forward iteration
        forwardSorted = False
        tempLargestNumber = None
        for key in range(len(nums) - 1):
            if nums[key] > nums[key + 1] and (tempLargestNumber is None or tempLargestNumber == nums[key]):
                tempLargestNumber = nums[key]
                nums[key], nums[key + 1] = nums[key + 1], nums[key]
        if (all(nums[i] <= nums[i + 1] for i in range(len(nums) - 1))):
            forwardSorted = True
            
        #Reverse(Backward) iteration   
        backwardSorted = False
        tempSmallestNumber = None
        for key in range(len(nums1) - 2, -1, -1):
            if nums1[key] > nums1[key + 1] and (tempSmallestNumber is None or tempSmallestNumber == nums1[key + 1]):
                tempSmallestNumber = nums1[key + 1]
                nums1[key], nums1[key + 1] = nums1[key + 1], nums1[key]
        if (all(nums1[i] <= nums1[i + 1] for i in range(len(nums1) - 1))):
            backwardSorted = True
    
        if (forwardSorted or backwardSorted):
            return True
        else:
            return False
