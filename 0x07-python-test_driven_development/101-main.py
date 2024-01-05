#!/usr/bin/python3
lazy_matrix_mul = __import__('101-lazy_matrix_mul').lazy_matrix_mul

print(lazy_matrix_mul([[1, 2], [3, 4]], [[1, 2], [3, 4]]))
print(lazy_matrix_mul([[1, 2]], [[3, 4.0], [5, 6]]))

print(lazy_matrix_mul('Holberton', [[5, 6], [7, 8]]))
print(lazy_matrix_mul([[5, 6], [7, 8]], "Holberton"))
print(lazy_matrix_mul([[]], [[5, 6], [7, 8]]))
print(lazy_matrix_mul([[5, 6], [7, 8]], [[]]))
print(lazy_matrix_mul([[5, "6"], [7, 8]], [[5, 6], [7, 8]]))
print(lazy_matrix_mul([[5, 6], [7, 8]], [[5, "6"], [7, 8]]))
print(lazy_matrix_mul([[5, 6, 10], [7, 8]], [[5, 6], [7, 8]]))
print(lazy_matrix_mul([[5, 6], [7, 8]], [[5, 6, 1], [7, 8]]))
print(lazy_matrix_mul([[1, 2, 3], [3, 4, 5]], [[1, 2], [3, 4]]))
