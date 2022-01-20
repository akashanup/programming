import math


class Solution:
    def isValidSpeed(self, piles, h, k):
        i = 0
        while i < len(piles):
            # If at any pile, the number of hours is exhausted then that speed is definitely not valid.
            if h <= 0:
                return False
            # To eat a pile of bananas with k speed, Koko would take (piles[i] / k) amount if time.
            if piles[i] > k:
                h -= math.ceil(piles[i] / k)
            else:
                """
                    Since Koko can eat a max of one pile per hour then,
                    If now all the piles have less number of bananas than the speed k, then we could simply check whether we have enough hours to finish all the piles. 
                    This is done to minimise the number of iteration of the loop.
                """
                return h >= len(piles) - i
            i += 1
        return h >= 0

    def binarySearch(self, piles, h, start, end):
        while start < end:
            mid = start + ((end - start) // 2)
            """
                If mid is a valid speed(potential answer) then mid could be an answer but we want to find the minimum of all potential answers so we will shrink our range for binary search such that end is mid now.
                Note: we are not doing mid - 1 because mid could be the required speed.
                If mid is not a valid speed then we will simply check for higher speed.
            """
            if self.isValidSpeed(piles, h, mid):
                end = mid
            else:
                start = mid + 1
        return start

    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        if len(piles) == h:
            return max(piles)
        totalBananas = sum(piles)
        if len(piles) == 1:
            return math.ceil(totalBananas / h)
        if totalBananas <= h:
            return 1
        piles.sort(reverse=True)
        """
            Minimum speed(potential answer) could be total number of bananas divided by total hours.
            Maximum speed(potential answer) must be the highest number of bananas in a pile.
            Required minimum speed would lie in the range of above two quatities.
            Now we have a sorted range of numbers and we have to find a number within that range based on some conditions, so we could think of binary search.
        """
        return self.binarySearch(piles, h, math.ceil(totalBananas / h), piles[0])
