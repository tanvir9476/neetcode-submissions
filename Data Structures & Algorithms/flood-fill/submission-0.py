class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
        ROWS, COLS = len(image), len(image[0])

        original_color = image[sr][sc]

        def dfs(r, c, visited):
            if (r < 0 or c < 0 or
                r > ROWS - 1 or c > COLS - 1 or
                image[r][c] != original_color or
                (r, c) in visited):
                return
            
            if image[r][c] == original_color:
                image[r][c] = color
                visited.add((r,c))

            dfs(r+1, c, visited)
            dfs(r-1, c, visited)
            dfs(r, c+1, visited)
            dfs(r, c-1, visited)

        dfs(sr, sc, set())
        return image


