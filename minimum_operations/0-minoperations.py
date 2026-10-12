#!/usr/bin/python3


def minOperations(n: int) -> int:
    if n <= 1:
        return 0

    operations = 0
    factor = 2

    while factor * factor <= n:
        while n % factor == 0:
            operations += factor
            n //= factor
        factor += 1

    # Any remaining value greater than 1 is prime
    if n > 1:
        operations += n

    return operations
