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

class Solution:
    # @param A : tuple of integers
    # @return an integer
    def maxSubArray(self, A):
        #kadane's algo
        sum_ = 0
        max_sum = float('-inf')
        for num in A:
            sum_ += num
            print("sum__",sum_)
            max_sum = max(sum_,max_sum)
            print("max_sum",max_sum)
            if sum_<0:
                print("+++++")
                sum_ = 0
        return max_sum

A = [-7,-4,-3,-1]
solution_instance = Solution()
max_sum=solution_instance.maxSubArray(A)
print(max_sum)