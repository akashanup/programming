class Solution:
    def checkArithmeticSubarrays(self, nums: List[int], l: List[int], r: List[int]) -> List[bool]:
        result = [False]*len(l)
        for i in range(len(result)):
            arr = sorted(nums[l[i]:r[i]+1])
            currResult = True
            if len(arr) < 2:
                currResult = False
            else:
                d = arr[1]-arr[0]
                for j in range(2, len(arr)):
                    if d != arr[j]-arr[j-1]:
                        currResult = False
                        break
            result[i] = currResult
        return result
