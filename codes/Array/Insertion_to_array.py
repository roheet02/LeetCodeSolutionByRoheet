"""
Author: Rohit Fuke
Description: Demonstrates basic array operations using Python's array module and NumPy,
             including insertion, traversal, access, search, and deletion.
"""

import array
import numpy as np

# ------------------------------------------------------
# 1. NumPy Array Example
# ------------------------------------------------------

# Creating a NumPy array
np_array = np.array([1, 2, 3, 4, 5, 6])
print("NumPy Array:")
print(np_array)  # Output: [1 2 3 4 5 6]

# ------------------------------------------------------
# 2. Inserting Element in Python's array
# ------------------------------------------------------

# Creating an integer array
my_array = array.array("i", [1, 2, 3, 4, 5])

# Inserting 11 at index 0
my_array.insert(0, 11)  # Time complexity: O(n) due to shifting elements
print("\nAfter Insertion at index 0:")
print(my_array)  # Output: array('i', [11, 1, 2, 3, 4, 5])

# ------------------------------------------------------
# 3. Traversing the Array
# ------------------------------------------------------

def traverse_array(arr):
    """
    Traverse and print elements of the array.
    Time Complexity: O(n)
    """
    print("\nTraversing Array:")
    for element in arr:
        print(element)  # O(1) for each element

traverse_array(my_array)

# ------------------------------------------------------
# 4. Accessing Element by Index
# ------------------------------------------------------

def access_element(arr, index):
    """
    Access an element from the array at a given index.
    Time Complexity: O(1)
    """
    print(f"\nAccessing element at index {index}:")
    if index >= len(arr):
        print("No element at this index.")
    else:
        print(arr[index])

access_element(my_array, 6)  # Out of bounds example

# ------------------------------------------------------
# 5. Searching for an Element (Method 1: using `in` and `index()`)
# ------------------------------------------------------

def search_element_builtin(arr, num):
    """
    Search using 'in' and 'index' methods.
    Time Complexity: O(n)
    """
    print(f"\nSearching for {num} using built-in methods:")
    if num in arr:
        print(f"Element found at index: {arr.index(num)}")
    else:
        print("Element not found.")

search_element_builtin(my_array, 6)

# ------------------------------------------------------
# 6. Searching for an Element (Method 2: Linear Search)
# ------------------------------------------------------

def search_element_manual(arr, target):
    """
    Linear search implementation.
    Time Complexity: O(n)
    """
    print(f"\nSearching for {target} using manual loop:")
    for i in range(len(arr)):
        if arr[i] == target:
            return f"Element found at index: {i}"
    return "Element not found."

print(search_element_manual(my_array, 3))

# ------------------------------------------------------
# 7. Deleting an Element
# ------------------------------------------------------

# Creating a new array for deletion example
del_array = array.array("i", [1, 2, 3, 4, 5])

# Removing element with value 1
del_array.remove(1)  # Time complexity: O(n)
print("\nAfter removing element 1:")
print(del_array)  # Output: array('i', [2, 3, 4, 5])
