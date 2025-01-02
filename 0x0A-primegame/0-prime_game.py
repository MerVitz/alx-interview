#!/usr/bin/python3
"""
Function that simulates the Prime Game between Maria and Ben.

Parameters:
    x (int): Number of rounds to play.
    nums (list of int): List of integers re
    presenting the value of n for each round.

Returns:
    str: The name of the player who won the most rounds, or
    None if there's a tie.
"""


def sieve_of_eratosthenes(limit):
    """Generates a list of pri
    mes and cumulative prime counts up to `limit`.
    """
    sieve = [True] * (limit + 1)
    sieve[0] = sieve[1] = False  # 0 and 1 are not primes
    for num in range(2, int(limit ** 0.5) + 1):
        if sieve[num]:
            for multiple in range(num * num, limit + 1, num):
                sieve[multiple] = False
    prime_count = [0] * (limit + 1)
    count = 0
    for i in range(limit + 1):
        if sieve[i]:
            count += 1
        prime_count[i] = count
    return prime_count


def isWinner(x, nums):
    """Determines the winner of `x` rounds based on the game rules."""
    if x == 0:
        return None  # No rounds to play, return None

    max_n = max(nums)
    prime_count = sieve_of_eratosthenes(max_n)

    maria_wins = 0
    ben_wins = 0

    # Process each round
    for n in nums:
        if prime_count[n] % 2 == 1:
            maria_wins += 1
        else:
            ben_wins += 1

    # Determine the overall winner
    if maria_wins > ben_wins:
        return "Maria"
    elif ben_wins > maria_wins:
        return "Ben"
    else:
        return None
