from sortedcontainers import SortedList


class Solution:
    def containsNearbyAlmostDuplicate(self, nums: List[int], k: int, t: int) -> bool:
        window = SortedList()
        for i in range(len(nums)):
            if i > k:
                window.remove(nums[i - k - 1])
            pos1 = SortedList.bisect_left(window, nums[i] - t)
            pos2 = SortedList.bisect_right(window, nums[i] + t)

            if pos1 != pos2 and pos1 != len(window):
                return True

            window.add(nums[i])

        return False
