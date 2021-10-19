class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        """
            We need to find all the distinct triplets for which their sum must be zero.
            So let's sort our array and then fix each number one by one and use two pointer technique to find the remainng two numbers for which their sum is zero.
            Till here the question is pretty straight forward, but it will fail for larger inputs having multiple duplicates.
            But you can see that from the given examples(or take any example on your own where there are multiple duplicates) that any triplet having sum as zero must have atleast one number different from other two.
            Exception: Only 0,0,0 will be a triplet whose sum is 0 and all values are same.
            So to overcome TLE, we need to filter out the duplicates if the number of duplicates is greater than 2 and greater than 3 for 0 value.
        """
        hashmap = {}
        for i in nums:
            if i not in hashmap:
                hashmap[i] = 1
            elif i != 0 and hashmap[i] < 2:
                hashmap[i] += 1
            elif i == 0 and hashmap[i] < 3:
                hashmap[i] += 1

        nums = []
        for num in hashmap:
            for i in range(hashmap[num]):
                nums.append(num)

        nums.sort()
        output = set()
        for i in range(len(nums)):
            start, end = 0, len(nums) - 1
            while start < end:
                if start == i:
                    start += 1
                elif end == i:
                    end -= 1
                else:
                    if nums[i] + nums[start] + nums[end] == 0:
                        output.add(tuple(sorted([nums[i], nums[start], nums[end]])))
                        start += 1
                        end -= 1
                    elif nums[i] + nums[start] + nums[end] > 0:
                        end -= 1
                    else:
                        start += 1
        return output
