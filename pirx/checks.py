#!/usr/bin/env python
import socket
import sys


def host(name):
    return socket.gethostname() == name

def arg(name, value=None):
    args = [arg.split('=') for arg in sys.argv[1:]]
    for arg_ in args:
        if arg_[0].lstrip('--') == name:
            if len(arg_) > 1:
                return arg_[1] == value
            else:
                return True
    return False

