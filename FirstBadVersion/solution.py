# The isBadVersion API is already defined for you.
# @param version, an integer
# @return an integer
# def isBadVersion(version):

class Solution:
    def firstBadVersion(self, n):
        """
        :type n: int
        :rtype: int
        """
        start = 1
        while start < n:
            mid = start + ((n - start) // 2)
            if isBadVersion(mid):
                n = mid
            else:
                start = mid + 1
        return n
