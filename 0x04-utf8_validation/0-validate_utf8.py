#!/usr/bin/python3
"""
UTF-8 Validation
"""


def validUTF8(data):
    """
    Determines if a given data set represents a valid UTF-8 encoding.

    Args:
        data (list): List of integers representing the dataset.

    Returns:
        bool: True if data is a valid UTF-8 encoding, False otherwise.
    """
    # Number of bytes left to process in the current character
    bytes_to_process = 0

    # Iterate over each integer in the data
    for num in data:
        # Mask the integer to only work with the 8 least significant bits
        byte = num & 0xFF

        if bytes_to_process == 0:
            # Determine the number of bytes in the character
            if byte >> 7 == 0:  # 1-byte character (0xxxxxxx)
                continue
            elif byte >> 5 == 0b110:  # 2-byte character (110xxxxx)
                bytes_to_process = 1
            elif byte >> 4 == 0b1110:  # 3-byte character (1110xxxx)
                bytes_to_process = 2
            elif byte >> 3 == 0b11110:  # 4-byte character (11110xxx)
                bytes_to_process = 3
            else:
                return False  # Invalid starting byte
        else:
            # Check that the byte starts with '10'
            if byte >> 6 != 0b10:
                return False
            bytes_to_process -= 1

    # If all characters are processed and
    #no bytes are left to process, it's valid
    return bytes_to_process == 0
