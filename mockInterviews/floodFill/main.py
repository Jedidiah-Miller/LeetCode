class Solution:
    def floodFill(self, image: [[int]], sr: int, sc: int, newColor: int) -> [[int]]:
        if image[sr][sc] == newColor:
            return image

        self.fill(image, sr, sc, image[sr][sc], newColor)
        return image

    def fill(self, image: [[int]], i: int, j: int, color: int, newColor: int):
        if i < 0 or i >= len(image) or j < 0 or j >= len(image[i]) or image[i][j] != color:
            return
        image[i][j] = newColor
        self.fill(image, i + 1, j, color, newColor) # down
        self.fill(image, i - 1, j, color, newColor) # up
        self.fill(image, i, j + 1, color, newColor) # right
        self.fill(image, i, j - 1, color, newColor) # left

# another solution i liked
    def _floodFill(self, image: [[int]], sr: int, sc: int, newColor: int) -> [[int]]:
        color = image[sr][sc]
        if color == newColor:
            return image
        R, C = len(image), len(image[0])
        def dfs(r, c):
            if image[r][c] == color:
                image[r][c] = newColor
                if r >= 1: dfs(r-1, c)
                if r + 1 < R: dfs(r+1, c)
                if c >= 1: dfs(r, c-1)
                if c + 1 < C: dfs(r, c+1)

        dfs(sr, sc)
        return image

image = [
    [1, 1, 1],
    [1, 1, 0],
    [1, 0, 1]
]

sr = 1
sc = 1
newColor = 2

Output: [
    [2, 2, 2],
    [2, 2, 0],
    [2, 0, 1]
]