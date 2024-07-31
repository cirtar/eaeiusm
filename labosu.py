def linear_search(arr, target):
    for i in range(len(arr)):
        if arr[i] == target:
            return i
    return -1

# Example usage
arr = [64, 34, 25, 12, 22, 11, 90]
index = linear_search(arr, 25)
print("Index of 25 using Linear Search:", index)
