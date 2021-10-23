class Solution:
    def reverse(self, nums, start, end):
        while start < end:
            nums[start], nums[end] = nums[end], nums[start]
            start += 1
            end -= 1

    def rotate(self, nums, k: int) -> None:
        n = len(nums)
        if n > 1 and k > 0:
            # If an array of length n is rotated by n steps then the result will be the original array.
            k = k % n
            """
                Rotating an array by k steps means-
                k rotated arr => arr[n-k:] + arr[:n-k]
                
                Now how to get the above two partitions of the array-
                    Let's reverse the entire array first and call it as arr1.
                    
                    Now, arr1[:k] will have the elements equal to arr[n-k:] but in reverse order
                    and arr1[k:] will have the elements equal to arr[:n-k] but in reverse order
                    Now to get the desired result we just need to reverse arr1[:k] and arr2[k:]                 
            """
            self.reverse(nums, 0, n-1)
            self.reverse(nums, 0, k-1)
            self.reverse(nums, k, n-1)
        return nums
