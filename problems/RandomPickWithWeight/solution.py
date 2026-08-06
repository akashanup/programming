class Solution:

    def __init__(self, w: List[int]):
        self.w = w
        for i in range(1, len(w)):
            self.w[i] += self.w[i-1]

    def binarySearch(self, target):
        left = 0
        right = len(self.w)-1
        while left < right:
            mid = left + ((right-left)//2)
            if self.w[mid] >= target:
                right = mid
            else:
                left = mid+1
        return left

    def pickIndex(self) -> int:
        rndNum = random.randint(1, self.w[-1])
        return self.binarySearch(rndNum)


# Your Solution object will be instantiated and called as such:
# obj = Solution(w)
# param_1 = obj.pickIndex()
