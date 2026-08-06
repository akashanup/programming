class Solution:
    def findDifferentBinaryString(self, nums: List[str]) -> str:
        binaryNumsString = set(nums)
        for decimalNum in range((2**len(nums))+1):
            binaryString = bin(decimalNum)[2:]
            binaryString = "0"*(len(nums)-len(binaryString)) + binaryString
            if binaryString not in binaryNumsString:
                return binaryString