#!/usr/bin/python3
"""Log parsing"""

from sys import stdin

status_codes = {
    "200": 0,
    "301": 0,
    "400": 0,
    "401": 0,
    "403": 0,
    "404": 0,
    "405": 0,
    "500": 0
}

file_size = 0


def print_logs():
    """Print logs"""
    print("File size: {}".format(file_size))
    for status in sorted(status_codes.keys()):
        if status_codes[status]:
            print("{}: {}".format(status, status_codes[status]))


if __name__ == "__main__":
    count = 0
    try:
        for line in stdin:
            if len(line) >= 3:
                parsed_items = line.split()
                s_code = parsed_items[-2]
                size = parsed_items [-1]
                if s_code in status_codes:
                    status_codes[s_code] += 1
                file_size += int(size)
            if count % 10 == 0:
                print_logs()
                count = -1
            count += 1
    except KeyboardInterrupt:
        print_logs()
        raise
    print_logs()
