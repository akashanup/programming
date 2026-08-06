"""
# Intuition
To maximize the sum of the minimum values in each pair, the best strategy is to pair numbers that are closest together.

After sorting the array:

- Adjacent elements form optimal pairs.
- The first element in every pair will be the minimum.
- So, we only need to add elements at even indices.

Since the constraints limit the values to: −104≤nums[i]≤104-10^4 \le nums[i] \le 10^4−104≤nums[i]≤104

we can use Counting Sort instead of comparison-based sorting to achieve linear time complexity.

# Approach
1. Create a frequency array to count occurrences of every number.
2. Use an offset of 10000 to handle negative values.
3. Traverse the frequency array in sorted order.
4. Alternate between:
    - taking a number into the answer,
    - skipping the next number.
5. This simulates pairing adjacent sorted elements efficiently.

# Complexity
- Time complexity: $$O(n+k)$$. Where:

    - n is the size of the input array.
    - k = 20001 is the fixed integer range.

This is effectively linear time.

- Space complexity: $$O(k)$$. A frequency array of size 20001 is used.
"""


class Solution:
    def arrayPairSum(self, nums: List[int]) -> int:
        offset = 10000
        freq = [0] * 20001

        for num in nums:
            freq[num + offset] += 1

        ans = 0
        take = True

        for i in range(20001):
            while freq[i] > 0:
                if take:
                    ans += i - offset

                take = not take
                freq[i] -= 1

        return ans