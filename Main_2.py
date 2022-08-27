from PIL import Image
from math import sqrt
import numpy as np

img = Image.open('Images/main.png')
qvazi_img = img.quantize(colors=5) 

img_colors = np.asarray(qvazi_img.convert('P', palette=1, colors=5))
ZERO_COLOR = 255
user_steps = 0

def dfs(grid, row, col, old_color, new_color):
    n = len(grid)
    m = len(grid[0])
    if row < 0 or row >= n or col < 0 or col >= m or grid[row][col] != old_color:
        return

    grid[row][col] = new_color
    dfs(grid, row+1, col, old_color, new_color)
    dfs(grid, row-1, col, old_color, new_color)
    dfs(grid, row, col+1, old_color, new_color)
    dfs(grid, row, col-1, old_color, new_color)

def flood_fill(grid, row, col, new_color):
    global user_steps
    user_steps += 1
    old_color = grid[row][col]
    if new_color == old_color:
        return
    dfs(grid, row, col, old_color, new_color)

_row_colors = lambda Values: [x for x in Values]
_rows = lambda Values: [_row_colors(x) for x in Values]

colors = _rows(img_colors)

print("Initial color schema:")
print(*colors, sep="\n")

#user steps  change color 
for idx, x in np.ndenumerate(colors):
    i, j = idx
    if colors[i][j] != ZERO_COLOR:
        flood_fill(colors, i, j, 255)

print("After changing color schema:")
print(*colors, sep="\n")

print("user_steps = ", user_steps)