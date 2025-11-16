# Function 1: Lists - Finding the Maximum and Second Maximum in a List
# This function takes a list of numbers as input and returns the maximum and second maximum values.
def max_two_in_list(numbers):
    if not numbers:
        return (None, None)
    try:
        first = second = None
        for n in numbers:
            if first is None or n > first:
                if first is not None and n != first:
                    second = first
                first = n
            elif n != first and (second is None or n > second):
                second = n
        return (first, second)
    except TypeError:
        return (None, None)

# Function 2: Lists - Removing Duplicates and Sorting
# This function takes a list of numbers and returns a sorted list with duplicates removed.
def remove_duplicates_and_sort(numbers):
    if not numbers:
        return []
    try:
        return sorted(set(numbers))
    except TypeError:
        # fallback for unhashable items (e.g., lists) — keep first occurrence order
        seen = []
        for x in numbers:
            if x not in seen:
                seen.append(x)
        return sorted(seen)

# Function 3: Single-Dimensional Arrays - Cumulative Sum
# This function takes an array (list) of numbers and returns a new list where each element is the cumulative sum of the previous elements.
def cumulative_sum(arr):
    out = []
    total = 0
    for n in arr:
        total += n
        out.append(total)
    return out

# Function 4: Two-Dimensional Arrays - Matrix Transpose
# This function takes a 2D list (matrix) and returns its transpose.
def transpose_matrix(matrix):
    if not matrix:
        return []
    return [list(row) for row in zip(*matrix)]
# Function 5: Slicing - Extracting Every Nth Element
# This function takes a list and a step value N and returns every Nth element.
def slice_every_nth(lst, step):
    
    return lst[::step]

# Function 6: Arithmetic Operations with Arrays - Dot Product
# This function takes two lists of the same length and returns their dot product.
def dot_product(list1, list2):
    
    return sum(a * b for a, b in zip(list1, list2))

# Function 7: Arithmetic Operations with Arrays - Matrix Multiplication
# This function takes two 2D lists (matrices) and returns their matrix product.
def matrix_multiplication(matrix1, matrix2):
    if not matrix1 or not matrix2 or len(matrix1[0]) != len(matrix2):
        return []

    rows = len(matrix1)
    cols = len(matrix2[0])
    inner = len(matrix2)

    result = [[0]*cols for _ in range(rows)]

    for i in range(rows):
        for j in range(cols):
            s = 0
            for k in range(inner):
                s += matrix1[i][k] * matrix2[k][j]
            result[i][j] = s

    return result