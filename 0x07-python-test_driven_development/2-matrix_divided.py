#!/urs/bin/python3
""" matrix divide by integer number """


def matrix_divided(matrix, div):
    """
    Divide The Whole Matrix by number
    Args:
        matrix (list of lists): list of lists of integers
        div (integer | floar): this is number will divide the matrix
    Returns:
        (list of lists) -> but it divided by div
    """
    error_message = "matrix must be list of lists of integer | float"
    if type(div) not in [float, int]:
        raise TypeError("div must be integer or float")
    if div == 0:
        raise ZeroDivisionError("division by zero")
    if type(matrix) is not list:
        raise TypeError(error_message)
    if len(matrix) == 0:
        raise TypeError("Empty Matrix")
    current_row_len = -1
    new_matrix = []
    index = -1
    for row in matrix:
        if not isinstance(row, list):
            raise TypeError(error_message)
        if len(row) == 0:
            raise TypeError("Empty Matrix")
        if current_row_len != -1 and current_row_len != len(row):
            raise TypeError("matrix must have same row and column")
        else:
            current_row_len = len(row)
        index += 1
        new_matrix.append([])
        for i in range(current_row_len):
            if type(row[i]) not in [float, int]:
                raise TypeError(error_message)
            new_matrix[index].append(row[i] / div)
    return new_matrix
