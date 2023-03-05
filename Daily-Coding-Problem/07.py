def count_decodings(message):
    if not message:
        return 0

    n = len(message)
    dp = [0] * (n + 1)
    dp[0] = 1
    dp[1] = 1 if message[0] != '0' else 0

    for i in range(2, n + 1):
        if message[i - 1] != '0':
            dp[i] += dp[i - 1]
        if message[i - 2:i] >= '10' and message[i - 2:i] <= '26':
            dp[i] += dp[i - 2]

    return dp[n]

print(count_decodings('111')) # Output: 3
print(count_decodings('12')) # Output: 2