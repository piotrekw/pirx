#!/usr/bin/env python
import socket
import sys


def host(name):
    """Check if host name is equal to the given name"""
    return socket.gethostname() == name

def arg(name, expected_value=None):
    """
    Check if command-line argument with a given name was passed and if it has
    the expected value.
    """
    args = [
        arg.split('=') for arg in sys.argv[1:] if '=' in arg else (arg, None)
    ]
    for arg_name, arg_value in args:
        if arg_name.lstrip('--') == name:
            return arg_value == expected_value
    return False

