#!/usr/bin/python3
"""The function prints the pascal triangle"""


def pascal_triangle(n):
    """The function prints Pascal triangle"""
    triangle = []
    if n <= 0:
        return triangle
    for i in range(n):
        empty = []
        for j in range(i + 1):
            if j == 0 or j == i:
                empty.append(1)
            else:
                empty.append(triangle[i-1][j-1] + triangle[i-1][j])
        triangle.append(empty)
    return triangle
