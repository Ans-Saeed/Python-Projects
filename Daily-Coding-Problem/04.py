def first_missing_positive(nums):
    n = len(nums)
    
    # Step 1: Convert non-positive integers to n + 1
    # We do this because since we're only interested in finding positive integers,
    # we can disregard all non-positive integers. We use n + 1 as a placeholder.
    for i in range(n):
        if nums[i] <= 0 or nums[i] > n:
            nums[i] = n + 1
    
    # Step 2: Mark visited integers as negative
    # For each number between 1 and n, we mark the (number - 1)th index as negative,
    # indicating that the number has been visited.
    # We ignore any numbers greater than n since we're only interested in positive integers.
    for i in range(n):
        num = abs(nums[i])
        if num <= n:
            nums[num - 1] = -abs(nums[num - 1])
    
    # Step 3: Find the first positive integer
    # If a positive integer is encountered, it means that the corresponding index
    # was not visited in step 2, so we return the index + 1 (as indices are 0-based).
    # If no positive integer is found, it means that all integers between 1 and n
    # were visited, so we return n + 1.
    for i in range(n):
        if nums[i] > 0:
            return i + 1
    
    return n + 1 