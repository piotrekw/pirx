#!/usr/bin/env python
import imp
import inspect
import sys

import pirx


def main():
    build_module = imp.load_module(sys.argv[1], *imp.find_module(sys.argv[1]))
    for name, obj in inspect.getmembers(build_module):
        if isinstance(obj, pirx.Settings):
            obj.write()
            break

if __name__ == '__main__':
    main()

