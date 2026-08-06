"""
Logic:
    1. As per the hints given for the problem, To minimize the number of operations we need to maximize the number of elements we keep from the original array. We will use this hint to build our solution.
    2. Check the below examples-
        a. Let's say we have an array [1,2,3,4,5] and one of the possible alternating array of this with minimum operations could be [1,2,1,2,1] (minimum operations: 3)
        b. Let's say we have another array [1,2,1,2,4,2] and one of the possible alternating array of this with minimum operations could be [1,2,1,2,1,2] (minimum operations: 1)
        c. Let's say we have another array [1,1,1,1,1,5,3,4,3] and one of the possible alternating array of this with minimum operations could be [3,1,3,1,3,1,3,1,3] (minimum operations: 5)
    3. What are we actually doing? We are actually calculating the minimum number of elements that needs to be altered to make the array alternating OR We are actually calculating the number of elements that need not to altered to make the array alternating.
    4. Below three conditions need to be satisfied for all elements of array:-
        a. Elements present at even index should be same.
        b. Elements present at odd index should be same
        c. Adjacent elements should not be same
    5. Now look closely at the above examples:-
        a. For example 2.a: Since all the numbers are different, we could fix any element at any even index and other element at any odd index. Let's say the elements present at 0th and 1st index are fixed and remaining elements are altered accordingly. Minimum number of operations required could be deduced as => len(nums) - max frequency of a number present at even index - max frequency of a number present at odd index, i.e., 5 - 1 - 1 = 3
        b. For example 2.b, we see that the max frequency for odd indexes is 3 for element 2 and max frequency for even indexes is 2 for element 1 and since the elements having the max frequency are not same so we should fix these elements and alter others. Therefore, minimum number of operations required => len(nums) - max frequency of a number present at even index - max frequency of a number present at odd index, i.e., 6 - 3 - 2 = 1
        c. For example 2.c, we see that the max frequency for odd indexes is 2 for element 1 and max frequency for even indexes is 3 for element 1 and since the elements having the max frequency are same so we can't fix these elements and alter others because it would contradict pt. 4.c. Therefore, we need to calculate the second maximum frequency for even and odd index. The second maximum frequency for odd index is 1 for element 5 and second maximum frequency for even index is 2 for element 3. Therefore, minimum number of operations required => len(nums) - max((max frequency of a number present at even index + second max frequency present at odd index), (max frequency of a number present at odd index + second max frequency of a number present at even index)), i.e., 9 - max(3+1, 2+2) = 9 - 4 = 5
"""


class Solution:
    def minimumOperations(self, nums: List[int]) -> int:
        even, odd = {}, {}
        maxEvenFreq, maxOddFreq = [None, 0], [None, 0]
        secondMaxEvenFreq, secondMaxOddFreq = [None, 0], [None, 0]

        for i, num in enumerate(nums):
            if i & 1:
                if num in odd:
                    odd[num] += 1
                else:
                    odd[num] = 1
            else:
                if num in even:
                    even[num] += 1
                else:
                    even[num] = 1

        for num in odd:
            if odd[num] > maxOddFreq[1]:
                maxOddFreq, secondMaxOddFreq = [num, odd[num]], maxOddFreq
            elif odd[num] > secondMaxOddFreq[1]:
                secondMaxOddFreq = [num, odd[num]]

        for num in even:
            if even[num] > maxEvenFreq[1]:
                maxEvenFreq, secondMaxEvenFreq = [num, even[num]], maxEvenFreq
            elif even[num] > secondMaxEvenFreq[1]:
                secondMaxEvenFreq = [num, even[num]]

        if maxEvenFreq[0] != maxOddFreq[0]:
            return len(nums) - (maxEvenFreq[1] + maxOddFreq[1])
        else:
            return len(nums) - max(maxEvenFreq[1] + secondMaxOddFreq[1],  maxOddFreq[1] + secondMaxEvenFreq[1])
