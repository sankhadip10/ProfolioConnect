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

def reconstruct_from_diff(diff):
    arr = [0] * (len(diff) - 1)
    arr[0] = diff[0]
    for i in range(1, len(arr)):
        arr[i] = arr[i-1] + diff[i]
    return arr

# Sample array and queries
arr = [5, 10, 15]
diff = initialize_diff_array(arr)
print("++++++",diff)
# update_diff_array(diff, 0, 1, 5)
# arr_updated = reconstruct_from_diff(diff)
# print(arr_updated)  # [10, 15, 15]
