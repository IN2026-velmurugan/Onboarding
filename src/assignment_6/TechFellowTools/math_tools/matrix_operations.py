"""Functions to perform calculations on matrix."""

Matrix = list[list[float]]


def matrix_addition(matrix_a: Matrix, matrix_b: Matrix) -> Matrix:
    """Perform matrix addition.

    Args:
        matrix_a: First matrix to be added with.
        matrix_b: Second matrix to be added.

    Returns:
        Addition of two matrix.
    """
    return [
        [matrix_a[i][j] + matrix_b[i][j] for j in range(len(matrix_a[0]))]
        for i in range(len(matrix_a))
    ]


def matrix_multiplication(matrix_a: Matrix, matrix_b: Matrix) -> Matrix:
    """Perform matrix multiplication.

    Args:
        matrix_a: First matrix to be multiplied with.
        matrix_b: Second matrix to be multiplied.

    Returns:
        Multiplication of two matrix.
    """
    result: Matrix = [[0 for _ in range(len(matrix_b[0]))] for _ in range(len(matrix_a))]
    for i in range(len(matrix_a)):
        for j in range(len(matrix_b[0])):
            for k in range(len(matrix_b)):
                result[i][j] += matrix_a[i][k] * matrix_b[k][j]
    return result


def transpose(matrix: Matrix) -> Matrix:
    """Perform transpose of a matrix.

    Args:
        matrix: Matrix to be transposed.

    Returns:
        The transposed matrix.
    """
    return [list(row) for row in zip(*matrix)]


def determinant_2x2(matrix: Matrix) -> float:
    """Calculate the determinant of the 2x2 matrix.

    Args:
        matrix: Matrix for which the determinant to be found.

    Raises:
        ValueError: If the matrix is not 2x2.

    Returns:
        Determinant of the 2x2 matrix.
    """
    if len(matrix) != 2 or len(matrix[0]) != 2:
        raise ValueError("Only 2x2 matrices supported")
    return matrix[0][0] * matrix[1][1] - matrix[0][1] * matrix[1][0]


def inverse_2x2(matrix: Matrix) -> Matrix:
    """Calculate the inverse of the 2x2 matrix.

    Args:
        matrix: Matrix for which the inverse to be found.

    Raises:
        ValueError: If the determinant value is 0.

    Returns:
        Inverse of the 2x2 matrix.
    """
    det = determinant_2x2(matrix)
    if det == 0:
        raise ValueError("Matrix is singular")
    return [
        [matrix[1][1] / det, -matrix[0][1] / det],
        [-matrix[1][0] / det, matrix[0][0] / det],
    ]
