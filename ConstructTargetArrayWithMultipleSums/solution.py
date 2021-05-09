from sortedcontainers import SortedList

class Solution:
    def isPossible(self, target: List[int]) -> bool:
        '''
            "Backtracking"
            Find the largest number in the array, there's a unique way to compute its value in the previous stage.
            Keep doing so until
            (i) all numbers are equal to 1 --> True
            (ii) any number becomes negative --> False
        '''
        #target will be automatically sorted now.
        target = SortedList(target)
        targetSum = sum(target)
        
        while True:
            largestValue = target[-1]
            remainingSum = targetSum - largestValue
            
            if largestValue == 1 or remainingSum == 1:
                return True
            # largestValue is found after adding a number to remaining sum. 
            # So largestValue should be greater tham remaining sum.
            if largestValue < remainingSum or remainingSum == 0 or largestValue%remainingSum == 0:
                return False
            
            # previous value of largest value would be (largestValue - sum of remaining elements of array)
            previousValue = largestValue % remainingSum
            target.remove(largestValue)
            target.add(previousValue)
            
            #Update target sum
            targetSum = remainingSum + previousValue


        return True