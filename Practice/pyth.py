# def initialize_diff_array(arr):
#     diff = [0] * (len(arr) + 1)
#     diff[0] = arr[0]
#     for i in range(1, len(arr)):
#         diff[i] = arr[i] - arr[i-1]
#     return diff
#
# def update_diff_array(diff, i, j, value):
#     diff[i] += value
#     if j+1 < len(diff):
#         diff[j+1] -= value
#
# def apply_queries(diff, queries):
#     # Apply each query to the difference array
#     for i, j, value in queries:
#         update_diff_array(diff, i, j, value)
#
#
#
# def reconstruct_from_diff(diff):
#     arr = [0] * (len(diff) - 1)
#     arr[0] = diff[0]
#     for i in range(1, len(arr)):
#         arr[i] = arr[i-1] + diff[i]
#     return arr
#
# # Original array
# arr = [5, 10, 15, 20, 25]
#
# # Queries (i, j, value) - assume 0-indexed
# queries = [
#     (0, 2, 5),  # Add 5 to range [0, 2]
#     (1, 3, 10), # Add 10 to range [1, 3]
#     (3, 4, -5)  # Subtract 5 from range [3, 4]
# ]
#
# # Initialize difference array
# diff = initialize_diff_array(arr)

# Apply the queries
# apply_queries(diff, queries)
#
# # Reconstruct the final array
# arr_updated = reconstruct_from_diff(diff)
#
# print(arr_updated)  # This will print the updated array after applying all queries

# A = [10,20,30,40]
# rightMax =[0]*len(A)
#
# rightMax[-1] = A[-1]
# for i in range(len(A)-2, -1, -1):
#     print(i)
#     print(rightMax[i+1])
#     rightMax[i] = max(rightMax[i+1], A[i])

# max_sum = float('-inf')
# A = [-7,4,3,-2]
# for i in range(len(A)):
#     print("First Loop",i)
#     print("___________________________________")
#     for j in range(i,len(A)):
#         print("------>>Second Loop ",j)
#         current_sum = 0
#         for k in range(i,j+1):
#             print("Third loop",A[k])
#             current_sum += A[k]
#             print("current_sum",current_sum)
#         max_sum = max(max_sum,current_sum)
#         print("====================")

# class Solution:
#     # @param A : tuple of integers
#     # @return an integer
#     def maxSubArray(self, A):
#         #kadane's algo
#         sum_ = 0
#         max_sum = float('-inf')
#         for num in A:
#             sum_ += num
#             print("sum__",sum_)
#             max_sum = max(sum_,max_sum)
#             print("max_sum",max_sum)
#             if sum_<0:
#                 print("+++++")
#                 sum_ = 0
#         return max_sum
#
# A = [-7,-4,-3,-1]
# solution_instance = Solution()
# max_sum=solution_instance.maxSubArray(A)
# print(max_sum)

# def compute_prefix_sum(arr):
#     prefix_sum = [0] * (len(arr) + 1)  # Create an extra space to handle sum from arr[0] to arr[i] inclusively.
#     for i in range(1, len(prefix_sum)):
#         prefix_sum[i] = prefix_sum[i-1] + arr[i-1]
#     return prefix_sum
# def query_sum(prefix_sum, i, j):
#     return prefix_sum[j + 1] - prefix_sum[i]
# # Initial array
# arr = [3, 6, 2, 8]
#
# # Compute prefix sum array
# prefix_sum = compute_prefix_sum(arr)
# print(prefix_sum)
#
# # Queries represented as tuples (start_index, end_index)
# queries = [(1, 3)]
#
# # Answer queries using the prefix sum array
# for query in queries:
#     i, j = query
#     print(f"Sum of arr[{i}:{j}] is {query_sum(prefix_sum, i, j)}")

# A = [ [1, 2],[3, 4] ]
# for inner_list in A:
#     for num in inner_list:
#         print(num,end=" ")

# def sum_of_all_submatrices(matrix):
#     n = len(matrix)      #No of rows
#     m = len(matrix[0])   #No of coumns
#     total_sum = 0
#     for i1 in range(n):
#         for j1 in range(m):
#             for i2 in range(i1,n):
#                 for j2 in range(j1,m):
#                     submatrix_sum = 0
#                     for i in range(i1,i2+1):
#                         for j in range(j1,j2+1):
#                             print("Matrix", i, j,":",matrix[i][j])
#                             submatrix_sum +=matrix[i][j]
#                     total_sum += submatrix_sum
#                     print("+++++++++++",total_sum)
#
#
# matrix = [[1, 2,3,4], [3, 4,5,6],[7,8,9,10],[11,12,13,14]]
# sum_of_all_submatrices(matrix)


# def find_row_with_max_ones(matrix):
#     n = len(matrix)      # Number of rows in the matrix
#     m = len(matrix[0])   # Number of columns in the matrix
#     row_index = -1       # To keep track of the row with maximum 1's
#     max_ones_count = 0   # To keep track of the maximum count of 1's
#
#     # Start from the top-right corner of the matrix
#     row = 0
#     col = m - 1
#
#     # Iterate over the matrix to find the row with the maximum number of 1's
#     while row < n and col >= 0:
#         # Move left if current element is 1
#         if matrix[row][col] == 1:
#             max_ones_count = col + 1  # Update the count of 1's in the current row
#             row_index = row          # Update the row index with the current row
#             col -= 1                 # Move left
#         # Move down if current element is 0
#         else:
#             row += 1  # Move down to the next row
#
#     return row_index, max_ones_count
#
# # Example usage
# matrix = [
#     [0, 0, 0, 0, 1],
#     [0, 0, 0, 1, 1],
#     [0, 0, 1, 1, 1],
#     [0, 1, 1, 1, 1],
#     [1, 1, 1, 1, 1]  # This row has the maximum number of 1's
# ]
#
# row_with_max_ones, max_ones = find_row_with_max_ones(matrix)
# print(f"Row {row_with_max_ones} has the maximum number of 1's: {max_ones}")
#
#
def find_frequencies(arr):
    n = len(arr)
    # Count the frequency
    for i in range(n):
        arr[arr[i] % n] += n
        print("arr[i]%n",arr[i],"%" ,n)
        print(arr)

    # Calculate the frequency
    frequency = [arr[i] // n for i in range(n)]
    print("frequency",frequency)

    # Optional: Restore original array values
    for i in range(n):
        arr[i] %= n
    return frequency



# Example Usage
arr = [1, 2, 2, 0]
print(arr)
print(find_frequencies(arr))


class Solution:
    def garbageCollection(self, garbage: List[str], travel: List[int]) -> int:
        total_minutes = 0  # Total minutes needed for garbage collection
        current_travel_time = 0  # Current travel time

        # Add the initial minutes required to collect garbage at the first house
        total_minutes += len(garbage[0])

        last_garbage_indices = [-1, -1, -1]  # Keep track of the last occurrence of each type of garbage

        # Iterate through each house starting from the second house
        for house_index in range(1, len(garbage)):
            # Add the minutes required to collect garbage at the current house
            total_minutes += len(garbage[house_index])

            # Update the indices of the last occurrence of each type of garbage
            if "M" in garbage[house_index]:
                last_garbage_indices[0] = house_index - 1
            if "P" in garbage[house_index]:
                last_garbage_indices[1] = house_index - 1
            if "G" in garbage[house_index]:
                last_garbage_indices[2] = house_index - 1

        # Iterate through each travel segment
        for travel_index in range(len(travel)):
            # Add the current travel time
            current_travel_time += travel[travel_index]

            # Add the minutes required to collect garbage if a garbage truck is at the corresponding house
            for truck_index in range(3):
                if last_garbage_indices[truck_index] == travel_index:
                    total_minutes += current_travel_time

        return total_minutes

    class Solution:
        def countNicePairs(self, nums: List[int]) -> int:
            mod = 1000000007
            length = len(nums)
            for i in range(length):
                nums[i] = nums[i] - self.reverse(nums[i])
            nums.sort()
            res = 0
            i = 0
            while i < length - 1:
                count = 1
                while i < length - 1 and nums[i] == nums[i + 1]:
                    count += 1
                    i += 1
                res = (res % mod + (count * (count - 1)) // 2) % mod
                i += 1

            return int(res % mod)

        def reverse(self, num: int) -> int:
            rev = 0
            while num > 0:
                rev = rev * 10 + num % 10
                num //= 10
            return rev