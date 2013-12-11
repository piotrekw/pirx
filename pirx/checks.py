#!/usr/bin/env python
import socket
import sys


def host(name):
    return socket.gethostname() == name

def arg(name, expected_value=None):
    args = [
        arg.split('=') for arg in sys.argv[1:] if '=' in arg else (arg, None)
    ]
    for arg_name, arg_value in args:
        if arg_name.lstrip('--') == name:
            return arg_value == expected_value
    return False

