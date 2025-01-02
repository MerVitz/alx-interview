#!/usr/bin/python3
"""
Function that simulates the Prime Game between Maria and Ben.

Parameters:
    x (int): Number of rounds to play.
    nums (list of int): List of integers representing
    the value of n for each round.

Returns:
    str: The name of the player who won the most rounds,
    :or None if there's a tie.
"""


def sieve_of_eratosthenes(limit):
    """Generates a list of primes up to `limit`
    using the Sieve of Eratosthenes.
    """
    sieve = [True] * (limit + 1)
    sieve[0] = sieve[1] = False  # 0 and 1 are not primes
    for num in range(2, int(limit ** 0.5) + 1):
        if sieve[num]:
            for multiple in range(num * num, limit + 1, num):
                sieve[multiple] = False
    primes = [num for num, is_prime in enumerate(sieve) if is_prime]
    return primes


def isWinner(x, nums):
    """Determines the winner of `x` rounds based on the game rules."""
    if x == 0:
        return None  # No rounds to play, return None

    # Step 1: Use the sieve to find primes up to 10,000
    max_n = 10000
    primes = sieve_of_eratosthenes(max_n)

    maria_wins = 0
    ben_wins = 0

    # Step 2: Process each round
    for n in nums:
        # Skip if n is too small (i.e., no primes available)
        if n <= 1:
            ben_wins += 1  # If n <= 1, Ben wins by default
            continue

        # Create a set of available numbers from 1 to n
        available_numbers = set(range(1, n + 1))
        turn = 0  # 0 for Maria's turn, 1 for Ben's turn

        while True:
            # Find the smallest prime <= n that is still in the set
            current_prime = None
            for prime in primes:
                if prime <= n and prime in available_numbers:
                    current_prime = prime
                    break

            # If no prime is available, the current player loses
            if current_prime is None:
                if turn == 0:  # Maria's turn, so Ben wins
                    ben_wins += 1
                else:  # Ben's turn, so Maria wins
                    maria_wins += 1
                break

            # Remove the current prime and its multiples from the set
            for multiple in range(current_prime, n + 1, current_prime):
                if multiple in available_numbers:
                    available_numbers.remove(multiple)

            # Alternate turns
            turn = 1 - turn

    # Step 3: Return the winner
    if maria_wins > ben_wins:
        return "Maria"
    elif ben_wins > maria_wins:
        return "Ben"
    else:
        return None
