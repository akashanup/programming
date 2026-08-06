from functools import lru_cache


class Solution:
    def shortestSuperstring(self, words: List[str]) -> str:
        # TSP, DP
        n = len(words)
        w = [[0] * n for i in range(n)]
        for i in range(n):
            for j in range(n):
                for k in range(min(len(words[i]), len(words[j])), 0, -1):
                    if words[j].startswith(words[i][-k:]):
                        w[i][j] = k
                        break

        @lru_cache(None)
        def dp(nodes):
            if len(nodes) == 2:
                return words[nodes[0]]
            end = nodes[-1]
            end_idx = nodes.index(end)
            # remove the current ending nodes from nodes[:-1]
            nodes_wo_end = nodes[:end_idx] + nodes[end_idx + 1:-1]
            # words[end][w[node][end]:] will remove overlap part from the end node.
            return min((dp(nodes_wo_end + (node,)) + words[end][w[node][end]:] for node in nodes_wo_end), key=len)

        return min((dp(tuple(range(n)) + (node,)) for node in range(n)), key=len)
