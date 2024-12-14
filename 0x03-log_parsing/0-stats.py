import sys
from collections import defaultdict

# Initialize counters
status_codes = defaultdict(int)
total_size = 0

try:
    for line in sys.stdin:
        # Parse log line (e.g., IP - [timestamp] "GET ..." status size)
        parts = line.split()
        if len(parts) > 6:
            size = int(parts[-1])
            status = parts[-2]
            total_size += size
            status_codes[status] += 1

        # Print stats every 10 lines
        if sum(status_codes.values()) % 10 == 0:
            print(f"File size: {total_size}")
            for code, count in sorted(status_codes.items()):
                print(f"{code}: {count}")

except KeyboardInterrupt:
    # Handle Ctrl+C gracefully
    print(f"File size: {total_size}")
    for code, count in sorted(status_codes.items()):
        print(f"{code}: {count}")
    sys.exit(0)
