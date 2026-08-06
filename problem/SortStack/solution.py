from typing import List


class Solution:

    def sortedInsert(self, stack: List[int], num: int) -> None:
        if not stack or stack[-1] > num:
            stack.append(num)
        else:
            top = stack.pop()
            self.sortedInsert(stack, num)
            stack.append(top)

    def sortItems(self, stack: List[int]) -> None:
        if stack:
            top = stack.pop()
            self.sortItems(stack)
            self.sortedInsert(stack, top)

    def sortStack(self, stack: List[int]) -> List[int]:
        self.sortItems(stack)
        return stack


print(Solution().sortStack([2, -9, 3, - 7, 5]))
