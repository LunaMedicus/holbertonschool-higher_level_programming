#!/usr/bin/python3
# 101-lazy_matrix_mul.py
"""Defines a matrix multiplication function using NumPy."""
import numpy as np


def lazy_matrix_mul(m_a, m_b):
    """Return the multiplication of two matrices.

    Args:
        m_a (list of lists of ints/floats): The first matrix.
        m_b (list of lists of ints/floats): The second matrix.
    """

    try:
        return (np.matmul(m_a, m_b))
    except TypeError:
        raise ValueError("Scalar operands are not allowed, use '*' instead")
    except ValueError:
        arr_a = np.array(m_a)
        arr_b = np.array(m_b)
        shape_a = str(arr_a.shape).replace(" ", "")
        shape_b = str(arr_b.shape).replace(" ", "")
        raise ValueError("shapes {} and {} not aligned: {} (dim 1) != {} (dim 0)".format(
            shape_a, shape_b, arr_a.shape[1], arr_b.shape[0]))
