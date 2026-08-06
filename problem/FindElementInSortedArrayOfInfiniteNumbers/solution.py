class Solution:
    def searchPosition(self, nums: List[int], target: int) -> List[int]:
        """
            Since the length of array is infinite, so binary search can not be directly applied as we don't know the length of array.
            Moreover, we can not put all the elements of array in buffer memory because length is infinite which will overflow.
            So, a good practice would be taking the chunks of array and apply binary search.
            Now the question arises that what would be the size of chunk?
            Most efficient choice would be making the size of chunks dynamic.
            Start with the size of 2 then apply binary search, if target found then return else use the next chunk with double the size of previous.
            Doubling the size of chunks each time would take max of log(n) as 2, 4, 8, 16 ... would sum up to log(n) time.
        """
        start = 0
        end = 1
        # Efficiently finding the start and end (or the required chunk) by exploiting the fact that nums is sorted and if target > nums[end] then target would definitely not lie in nums[start:end] chunk.
        while target > nums[end]:
            newStart = end + 1
            end = newStart + ((end - start + 1) * 2)
            start = newStart
        # Apply binary search
        while start <= end:
            mid = start + ((end - start) // 2)
            if nums[mid] == target:
                return mid
            elif nums[mid] > target:
                end = mid - 1
            else:
                start = mid + 1
        return -1


print(Solution().searchPosition(nums = [1, 2, 3, 4, 5, 6, 7, 8], target = 7))
