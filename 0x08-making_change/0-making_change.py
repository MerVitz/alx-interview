#!/usr/bin/python3

"""
This is the module for making change
"""


def makeChange(coins, total):
    # Edge case: If the total is 0 or less, no coins are needed
    if total <= 0:
        return 0

    # Initialize the DP table with a large number (infinity)
    dp = [float('inf')] * (total + 1)

    # No coins are needed to make 0
    dp[0] = 0

    # Iterate over each coin in the list
    for coin in coins:
        for i in range(coin, total + 1):
            dp[i] = min(dp[i], dp[i - coin] + 1)

    # If dp[total] is still infinity, it means the total
    return dp[total] if dp[total] != float('inf') else -1
