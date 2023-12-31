
import numpy as np

# Creating NumPy arrays
arr1 = np.array([1, 2, 3, 4, 5])  # Create a 1-dimensional array
print("1D Array:")
print(arr1)

arr2 = np.array([[1, 2, 3], [4, 5, 6]])  # Create a 2-dimensional array
print("\n2D Array:")
print(arr2)

# Accessing elements in a NumPy array
print("\nAccessing Elements:")
print(arr1[0])          # Accessing a single element
print(arr2[1, 2])       # Accessing a single element from a 2D array
print(arr2[0])          # Accessing an entire row in a 2D array

# Slicing NumPy arrays
print("\nSlicing Arrays:")
print(arr1[1:4])        # Slicing a 1D array
print(arr2[:, 1:])     # Slicing a 2D array

# Modifying elements in a NumPy array
arr1[3] = 8     # Modifying a single element
print("\nModified Array:")
print(arr1)

arr2[0, 2] = 9  # Modifying a single element in a 2D array
print("\nModified 2D Array:")
print(arr2)

# Array shape and reshaping
print("\nArray Shape and Reshaping:")
print(arr1.shape)                  # Shape of a 1D array
reshaped_arr = arr1.reshape((5, 1)) # Reshaping a 1D array into a 2D array
print(reshaped_arr)

# Array concatenation and splitting
arr3 = np.array([6, 7, 8])
concatenated_arr = np.concatenate((arr1, arr3))  # Concatenating two arrays
print("\nConcatenated Array:")
print(concatenated_arr)

split_arr = np.split(concatenated_arr, [3])  # Splitting an array into multiple sub-arrays
print("\nSplit Arrays:")
print(split_arr)
