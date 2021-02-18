#!/usr/bin/python3
""" 
UTF-8 validation
"""


def validUTF8(data):
    """ [validUTF8]: method that determines if a given data set represents a valid UTF-8 encoding
    """
    try:
        string = [n & 255 for n in data]
        bytes(string).decode("UTF-8")
        return True
    except UnicodeDecodeError:
        return False