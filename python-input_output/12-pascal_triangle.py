#!/usr/bin/python3
"""Defines a Pascal's Triangle function."""


def pascal_triangle(n):
    """Return a list of lists of integers representing Pascal's triangle."""
    if n <= 0:
        return []

    triangle = [[1]]
    while len(triangle) < n:
        previous_row = triangle[-1]
        row = [1]
        for index in range(len(previous_row) - 1):
            row.append(previous_row[index] + previous_row[index + 1])
        row.append(1)
        triangle.append(row)
    return triangle
