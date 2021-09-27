class Solution:
    def search(self, nums: List[int], target: int) -> bool:
        start = 0
        end = len(nums) - 1
        while start <= end:
            mid = start + ((end - start) // 2)
            """
                Update start and end pointers based on the different parts of array where target may lie.
                For example - Consider the following array:
                arr = [4, 5, 6, 7, 8, 1, 2, 3] 
                parts of array would be:
                1st part: 4-7
                2nd part: 8
                3rd part: 1-3
                Note: If nums[mid] == nums[start] then we can just skip the start value as we are just removing a duplicate value.
            """
            if nums[mid] == target:
                return True
            elif nums[start] == nums[mid]:
                start += 1
            elif nums[start] < nums[mid]:
                # 1st part of array i.e, if target lies in first part of array then search only in that part Else search in the remaining parts
                if nums[start] <= target < nums[mid]:
                    end = mid - 1
                else:
                    start = mid + 1
            else:
                # 3rd part of array i.e, if target lies in 3rd part then search only in that part Else search in the remaining parts.
                if nums[mid] < target <= nums[end]:
                    start = mid + 1
                else:
                    end = mid - 1
        return False
