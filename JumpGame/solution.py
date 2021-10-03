class Solution:
    def canJump(self, nums: List[int]) -> bool:
        n = len(nums)
        """
            If all the numbers are greater than zero or if there is only one number then we will definitely reach the last position.
        """
        if min(nums) > 0 or n == 1:
            return True
        """
            If the first number is zero then we can't move any further.
        """
        if nums[0] == 0:
            return False
        """
            Let's say we can reach maximum of {farthest} from the {current} location.
        """
        farthest = nums[0]
        current = nums[0]
        for num in range(1, n):
            if num == n-1:
                return True
            """
                For every jump, we are moving one step ahead by using {farthest} and {current} so {farthest} and {current} will be decremented by 1.
            """
            current -= 1
            farthest -= 1
            """
                If at any step, {farthest} becomes less then the value of current step then update {farthest} as we can now reach a farthest of value of current step.
            """
            if farthest < nums[num]:
                farthest = nums[num]
            """
                If at any point, our {current} is fully exhausted but we can still move a maximum of {farthest} so update our {current} with {farthest}
            """
            if current == 0:
                current = farthest
            """
                If we can't move any further then return False.
            """
            if farthest == 0:
                return False
