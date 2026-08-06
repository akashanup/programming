class Solution:
    def recur(self, arr, n, start):
        if arr[start] == 0:
            return True
        else:
            val = arr[start]
            arr[start] = None
            reached = False
            if 0 <= start + val < n and arr[start + val] is not None:
                if self.recur(arr, n, start + val):
                    reached = True
            if not reached:
                if 0 <= start - val < n and arr[start - val] is not None:
                    reached = self.recur(arr, n, start - val)
            return reached

    def canReach(self, arr: List[int], start: int) -> bool:
        return self.recur(arr, len(arr), start)
