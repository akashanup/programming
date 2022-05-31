class Solution:
    def dfs(self, rows, cols, r, c, visited):
        visited.add((r, c))
        for row, col in rows[r]:
            if (row, col) not in visited:
                self.dfs(rows, cols, row, col, visited)
        for row, col in cols[c]:
            if (row, col) not in visited:
                self.dfs(rows, cols, row, col, visited)

    def removeStones(self, stones: List[List[int]]) -> int:
        # Let's have two dicts rows and cols which will have coordinates of stone for each row and column where the stones are placed..
        rows, cols = {}, {}

        # Store the stones in dicts based on their row and col.
        for r, c in stones:
            if r not in rows:
                rows[r] = []
            rows[r].append((r, c))
            if c not in cols:
                cols[c] = []
            cols[c].append((r, c))

        connectedComponents = 0
        visited = set()
        # DFS to find out connected components i.e, for a particular (r,c) find the number of stones that lies either on row r or column c.
        for r, c in stones:
            if (r, c) not in visited:
                connectedComponents += 1
                self.dfs(rows, cols, r, c, visited)

            # Return total number of stones - total number of connected stones because we can remove the connected stones as given in the question and by substracting it, we will get total number of removed stones.
        return len(stones) - connectedComponents
