#!/usr/bin/python3
def minOperations(n):
    if n < 2:
        return 0  # Not possible to create less than 2 characters
    
    operations = 0
    factor = 2

    while n > 1:
        while n % factor == 0:
            operations += factor
            n //= factor
        factor += 1
    
    return operations

