def reverse_matrices(matrices):
    """
    This function takes a list of matrices and returns a new list with the order of the matrices reversed.
    
    Parameters:
    matrices (list of lists): A list where each element is a matrix (which is itself a list of lists).

    Returns:
    list of lists: A new list with the matrices in reversed order.
    """
    return matrices[::-1]

# Example usage
matrices = [
    [[1, 2], [3, 4]],
    [[5, 6], [7, 8]],
    [[9, 10], [11, 12]]
]

reversed_matrices = reverse_matrices(matrices)
print(reversed_matrices)
