# Given a list of integers, write a function that returns the largest sum of non-adjacent numbers. Numbers can be 0 or negative.

# For example, [2, 4, 6, 2, 5] should return 13, since we pick 2, 6, and 5. [5, 1, 1, 5] should return 10, since we pick 5 and 5.

# Follow-up: Can you do this in O(N) time and constant space?


def max_sum_non_adjacent(nums):
    # if the list is empty, return 0
    if not nums:
        return 0
    
    # if the list has only one element, return that element
    if len(nums) == 1:
        return nums[0]
    
    # initialize variables to keep track of the maximum sums
    prev_max = nums[0]  # maximum sum up to the previous element
    curr_max = max(nums[0], nums[1])  # maximum sum up to the current element
    
    # iterate over the list starting from the third element
    for i in range(2, len(nums)):
        # calculate the maximum sum up to the current element by choosing
        # whether to include the current element or not
        num = nums[i]
        prev_max, curr_max = curr_max, max(curr_max, prev_max + num)
    
    # return the maximum sum
    return curr_max