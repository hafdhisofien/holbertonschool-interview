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
            try:
                parsed_items = line.split()
                file_size += int(parsed_items[-1])
                if parsed_items[-2] in status_codes:
                    status_codes[parsed_items[-2]] += 1
            except:
                pass
            if count % 10 == 0:
                print_logs()
                count = -1
            count += 1
    except KeyboardInterrupt:
        print_logs()
        raise
    print_logs()