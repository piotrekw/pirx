#!/usr/bin/env python
import socket


def host(name):
    return socket.gethostname() == name

