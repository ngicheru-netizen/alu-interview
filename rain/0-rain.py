#!/usr/bin/python3
"""Calculate the amount of rainwater retained between walls."""


def rain(walls):
    """Return the total water retained by a list of wall heights."""
    if len(walls) < 3:
        return 0

    left = 0
    right = len(walls) - 1
    left_max = walls[left]
    right_max = walls[right]
    retained = 0

    while left < right:
        if left_max <= right_max:
            left += 1
            left_max = max(left_max, walls[left])
            retained += left_max - walls[left]
        else:
            right -= 1
            right_max = max(right_max, walls[right])
            retained += right_max - walls[right]

    return retained
