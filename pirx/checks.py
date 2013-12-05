#!/usr/bin/env python
import socket
import sys


def host(name):
    return socket.gethostname() == name

def arg(name, value=None):
    args = [arg.split('=') for arg in sys.argv[1:]]
    for arg in args:
        if arg[0].lsplit('--') == name:
            if len(arg) > 1:
                return arg[1] == value
            else:
                return True

