def longest_sub_string(s,k):
    n = len(s)
    freq = {}
    left = right = max_len = 0
    
    while right < n:
        # Expand the window to the right
        if s[right] not in freq:
            freq[s[right]] = 0
        freq[s[right]] += 1
        
        # Shrink the window from the left if needed
        while len(freq) > k:
            freq[s[left]] -= 1
            if freq[s[left]] == 0:
                del freq[s[left]]
            left += 1
        
        # Update the maximum length
        max_len = max(max_len, right - left + 1)
        
        # Move the window to the right
        right += 1
    print (freq.values())
    return max_len


print (longest_sub_string("abcba",2))