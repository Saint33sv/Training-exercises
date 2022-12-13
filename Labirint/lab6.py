import cv2
import matplotlib.pyplot as plt
import numpy as np
from collections import deque


def get_distance(img, u, v):
    return 0.1 + (float(img[v][0]) - float(img[u][0])) ** 2 + (float(img[v][1]) - float(img[u][1])) ** 2 + \
                (float(img[v][2]) - float(img[u][2])) ** 2


def get_neighbors(mat, x, y):
    """Координаты пикселя это индекс столбца матрицы-x и рядка-y"""
    shape = mat.shape
    neighbors = []
    if x > 0 and mat[y][x-1]:
        neighbors.append(mat[y][x-1])
    if x < shape[1]-1 and mat[y][x+1]:
        neighbors.append(mat[y][x+1])
    if y > 0 and mat[y-1][x]:
        neighbors.append(mat[y-1][x])
    if y < shape[0]-1 and mat[y+1][x]:
        neighbors.append(mat[y+1][x])
    return neighbors


def shortest_path(picture, start_c, finish_c):
    # """Старт и финиш это кортежи типа (x, y)"""
    S = {}
    V = {}
    imagerows, imagecols = picture.shape[0], picture.shape[1]
    matrix = np.full((imagerows, imagecols), None)  # доступ по матрице[строка][столбец]
    for r in range(imagerows):
        for c in range(imagecols):
            matrix[r][c] = (c, r)
    pq = deque([start_c])
    S[start_c] = 0
    while pq:
        cur_node = pq.popleft()
        neighbors = get_neighbors(matrix, cur_node[0], cur_node[1])
        for neighbor in neighbors:
            distance = get_distance(img, (cur_node[1], cur_node[0]), (neighbor[1], neighbor[0]))
            if neighbor not in pq or S[cur_node]+distance < S[neighbor]:
                S[neighbor] = S[cur_node]+distance
                V[neighbor] = cur_node
                pq.append(neighbor)
    print(S)
    # path = []
    # pixel = finish_c
    # while pixel != start_c:
    #     path.append(pixel)
    #     pixel = V[pixel]
    # path.append(start_c)
    # return path


def drow_path(picture, path):
    x0, y0 = path[0][0], path[0][1]
    for pixel in path[1:]:
        x1, y1 = pixel[0], pixel[1]
        cv2.line(picture, (x0, y0), (x1, y1), (0, 0, 255), thickness=1)
        x0, y0 = pixel[0], pixel[1]


img = cv2.imread('lab.png')
shortest_path(img, (25, 5), (8, 220))
# drow_path(img, path)
# plt.figure(figsize=(7, 7))
# plt.imshow(img)
# plt.show()
