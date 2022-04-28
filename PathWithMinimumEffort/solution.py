class Solution:
    def canReachToEnd(self, graph, k, visited, src, dest):
        visited[src] = True
        if src == dest:
            return True
        for u in graph[src]:
            if not visited[u[0]] and u[1] <= k and self.canReachToEnd(graph, k, visited, u[0], dest):
                return True
        return False
                
        
    def minimumEffortPath(self, heights: List[List[int]]) -> int:
        rows, cols = len(heights)-1, len(heights[0])-1
        if rows == 0 and cols == 0:
            return 0
        
        graph = [None] * ((rows+1) * (cols+1))
        left, right = sys.maxsize, -sys.maxsize

        for r in range(rows+1):
            for c in range(cols+1):
                if r > 0:
                    u = r * cols
                else:
                    u = 0
                u += r + c
                graph[u] = []
                # Left
                if c > 0:
                    v = u-1
                    weight = abs(heights[r][c] - heights[r][c-1])
                    right = max(right, weight)
                    left = min(left, weight)
                    graph[u].append([v, weight])
                # Right
                if c < cols:
                    v = u+1
                    weight = abs(heights[r][c] - heights[r][c+1])
                    right = max(right, weight)
                    left = min(left, weight)
                    graph[u].append([v, weight])
                # Top
                if r > 0:
                    v = u - (cols+1)
                    weight = abs(heights[r][c] - heights[r-1][c])
                    right = max(right, weight)
                    left = min(left, weight)
                    graph[u].append([v, weight])
                
                # Down
                if r < rows:
                    v = u + (cols+1)
                    weight = abs(heights[r][c] - heights[r+1][c])
                    right = max(right, weight)
                    left = min(left, weight)
                    graph[u].append([v, weight])
        
        # Binary search the value of minimum effort(k) between left and right
        while left < right:
            mid = left + ((right-left)//2)
            visited = [False]*len(graph)
            if self.canReachToEnd(graph, mid, visited, 0, len(graph)-1):
                right = mid
            else:
                left = mid + 1
        
        return right
