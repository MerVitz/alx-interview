#!/usr/bin/python3
"""
Script that reads stdin line by line and computes metrics:
- File size
- Counts of status codes
"""

import sys


def print_stats(total_size, status_counts):
    """
    Print the cumulative file size and status code counts
    """
    print(f"File size: {total_size}")
    for code in sorted(status_counts.keys()):
        print(f"{code}: {status_counts[code]}")


# Initialize counters
total_size = 0
status_counts = {}

# Valid status codes
valid_codes = ['200', '301', '400', '401', '403', '404', '405', '500']

try:
    for i, line in enumerate(sys.stdin, 1):
        # Split the line into parts
        parts = line.split()

        # Parse the file size (last element)
        try:
            total_size += int(parts[-1])
        except (IndexError, ValueError):
            continue  # Skip lines without a valid file size

        # Parse the status code (second-to-last element)
        try:
            status_code = parts[-2]
            if status_code in valid_codes:
                status_counts[status_code] = (
                    status_counts.get(status_code, 0) + 1
                )
        except IndexError:
            continue  # Skip lines without a valid status code

        # Print stats every 10 lines
        if i % 10 == 0:
            print_stats(total_size, status_counts)

except KeyboardInterrupt:
    # Handle Ctrl+C gracefully
    pass

finally:
    # Print final stats at the end
    print_stats(total_size, status_counts)
