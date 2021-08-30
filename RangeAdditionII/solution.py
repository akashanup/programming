class Solution:
    def maxCount(self, m: int, n: int, ops: List[List[int]]) -> int:
        '''
            for x, y in ops:
                if x < m:
                    m = x
                if y < n:
                    n = y
            return m * n
        '''
        # Optimised
        if not ops:
            return m*n
        return min(op[0] for op in ops) * min(op[1] for op in ops)
