def initialize_diff_array(arr):
    diff = [0] * (len(arr) + 1)
    diff[0] = arr[0]
    for i in range(1, len(arr)):
        diff[i] = arr[i] - arr[i-1]
    return diff

def update_diff_array(diff, i, j, value):
    diff[i] += value
    if j+1 < len(diff):
        diff[j+1] -= value

def apply_queries(diff, queries):
    # Apply each query to the difference array
    for i, j, value in queries:
        update_diff_array(diff, i, j, value)



def reconstruct_from_diff(diff):
    arr = [0] * (len(diff) - 1)
    arr[0] = diff[0]
    for i in range(1, len(arr)):
        arr[i] = arr[i-1] + diff[i]
    return arr

# Original array
arr = [5, 10, 15, 20, 25]

# Queries (i, j, value) - assume 0-indexed
queries = [
    (0, 2, 5),  # Add 5 to range [0, 2]
    (1, 3, 10), # Add 10 to range [1, 3]
    (3, 4, -5)  # Subtract 5 from range [3, 4]
]

# Initialize difference array
diff = initialize_diff_array(arr)

# Apply the queries
apply_queries(diff, queries)

# Reconstruct the final array
arr_updated = reconstruct_from_diff(diff)

print(arr_updated)  # This will print the updated array after applying all queries
