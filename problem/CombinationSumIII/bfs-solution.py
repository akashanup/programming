from collections import deque


class Solution:
    def combinationSum3(self, k: int, n: int) -> List[List[int]]:
        candidates = [_ for _ in range(1, 10)]
        combinations = []
        queue = deque([])

        for idx, candidate in enumerate(candidates):
            queue.append([candidate, idx+1, [candidate]])

        while queue:
            currSum, idx, combination = queue.popleft()
            if currSum == n and len(combination) == k:
                combinations.append(combination)
            if len(combination) < k:
                for i in range(idx, len(candidates)):
                    if currSum + candidates[i] <= n:
                        queue.append([currSum + candidates[i], i+1, combination + [candidates[i]]])
        return combinations
