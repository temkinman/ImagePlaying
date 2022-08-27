from PIL import Image
from math import sqrt
import numpy as np
import random
from queue import Queue

img1 = Image.open('Images/main.png')

# quantize a image 
im1 = img1.quantize(5) 
  
print(im1)
# "Orange", "Grey", "Blue", "Green", "Brown"
COLORS = {
            "Orange" : [201,146,0],
            "Grey" : [151,151,153],
            "Blue" : [43,188,206],
            "Green" : [126,193,44],
            "Brown": [156, 107, 86]
          }

def get_closest_color(rgb):
    r = rgb[0]
    g = rgb[1]
    b = rgb[2]
    color_diffs = []
    for value in COLORS.values():
        cr, cg, cb = value
        color_diff = sqrt((r - cr)**2 + (g - cg)**2 + (b - cb)**2)
        color_diffs.append((color_diff, value))
    
    nearest_color = min(color_diffs)[1]    
    name_color = list(COLORS.keys())[list(COLORS.values()).index(nearest_color)]
    return name_color

# def flood_fill(grid, i, j, new_color):
#     n = len(grid)
#     m = len(grid[0])
#     old_color = grid[i][j]
#     if np.array_equal(old_color, new_color): #old_color == new_color:
#         return
#     queue = Queue()
#     queue.put((i, j))
#     while not queue.empty():
#         i, j = queue.get()
#         if i < 0 or i >= n or j < 0 or j >= m or not np.array_equal(grid[i][j], old_color): #grid[i][j] != old_color:
#             continue
#         else:
#             grid[i][j] = new_color
#             queue.put((i+1, j))
#             queue.put((i-1, j))
#             queue.put((i, j+1))
#             queue.put((i, j-1))

# def flood_recursive(matrix):
#     width = len(matrix)
#     height = len(matrix[0])
#     def fill(x,y,start_color,color_to_update):
#         #if the square is not the same color as the starting point
#         if matrix[x][y] != start_color:
#             return
#         #if the square is not the new color
#         elif matrix[x][y] == color_to_update:
#             return
#         else:
#             #update the color of the current square to the replacement color
#             matrix[x][y] = color_to_update
#             neighbors = [(x-1,y),(x+1,y),(x-1,y-1),(x+1,y+1),(x-1,y+1),(x+1,y-1),(x,y-1),(x,y+1)]
#             for n in neighbors:
#                 if 0 <= n[0] <= width-1 and 0 <= n[1] <= height-1:
#                     fill(n[0],n[1],start_color,color_to_update)
    
#     #pick a random starting point
#     start_x = random.randint(0,width-1)
#     start_y = random.randint(0,height-1)
#     start_color = matrix[start_x][start_y]
#     updated_color = [255, 255, 255]
#     fill(start_x,start_y,start_color,updated_color)
#     return matrix

image_colors = np.array(img1)

updated_color = [0, 0, 0, 0]
target_color = [149, 149, 151, 255]
# DFS approach:
def dfs(grid, i, j, old_color, new_color):
    n = len(grid)
    m = len(grid[0])
    if i < 0 or i >= n or j < 0 or j >= m or not np.array_equal(grid[i][j], old_color):
        return

    grid[i][j] = new_color
    dfs(grid, i+1, j, target_color, new_color)
    dfs(grid, i-1, j, target_color, new_color)
    dfs(grid, i, j+1, target_color, new_color)
    dfs(grid, i, j-1, target_color, new_color)

def flood_fill(grid, i, j, new_color):
    old_color = grid[i][j]
    if np.array_equal(new_color, old_color):
        return
    dfs(grid, i, j, old_color, new_color)

def print_matrix(matrix):
  for i in matrix:
      for j in i:
          print(j, end=" ")
      print()


# field = [
#     [[156 107  86 255], [149 149 151 255], [149 149 151 255], [149 149 151 255], [200 145 0 255], [200 145 0 255], [200 145 0 255], [156 107 86 255], [40 185 205 255], [126 193  43 255]]
#     [[ 41 189 207 255], [201 146   0 255], [151 151 153 255], [ 41 187 206 255], [152 151 150 255], [201 146   0 255], [ 41 187 205 255], [129 195  46 255], [200 146   1 255], [156 107  85 255]]
#     [[ 41 189 207 255], [201 146   0 255], [151 151 153 255], [ 41 187 206 255], [152 151 150 255], [201 146   0 255], [ 41 187 205 255], [129 195  46 255], [200 146   1 255], [156 107  85 255]]
    
# ]

# arr = [
#   []

# ]



print("Initial color schema:")
# print(image_colors)

arr2 = image_colors.copy()

# print("m[1] = ", image_colors[1])
# print("m[1][2] = ", image_colors[1][2])
print('------AFTER CHANGING--------')

flood_fill(image_colors, 0, 1, updated_color)
# print_matrix(image_colors)



# print(image_colors)

# for colors in image_colors:
#   for color in colors:
#       print(*color)
#     #   print(type(color))
#       closest_color = get_closest_color(color)
#       print(closest_color )
#   print('--------------')
# print(arr)
# print(arr.size)
# print(arr.shape)

