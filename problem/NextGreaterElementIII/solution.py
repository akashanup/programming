import heapq


class Solution:
    def nextGreaterElement(self, n: int) -> int:
        heap = []
        heapq.heapify(heap)
        n = str(n)
        i = len(n) - 1
        while i > 0:
            heapq.heappush(heap, n[i])
            if n[i] > n[i-1]:
                break
            i -= 1
        # n is reverse sorted
        if i == 0:
            return -1
        # Before this index, nothing needs to be changed.
        i -= 1
        pivotItem = n[i]
        n = n[:i]
        temp = ''
        while heap:
            '''
                Build the string of numbers in ascending order till the last number is less than or equal to pivot number.
                Once a number is found that is greater than pivot, append it to original string and then append the remaining in sorted order.
            '''

            poppedNum = heapq.heappop(heap)
            if pivotItem == '' or poppedNum <= pivotItem:
                temp += poppedNum
            else:
                n += poppedNum + temp + pivotItem
                pivotItem = ''
                temp = ''
        n += temp
        n = int(n)
        return n if (1 <= n <= (2**31) - 1) else -1
