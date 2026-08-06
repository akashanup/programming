class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
        if image[sr][sc] == color:
            return image

        initialColor = image[sr][sc]
        image[sr][sc] = color
        queue = deque([(sr, sc)])
        while queue:
            row, col = queue.popleft()
            for r, c in ((row+1, col), (row-1, col), (row, col+1), (row, col-1)):
                if 0 <= r < len(image) and 0 <= c < len(image[0]) and image[r][c] == initialColor:
                    image[r][c] = color
                    queue.append((r,c))

        return image
