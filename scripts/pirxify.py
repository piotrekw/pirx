#!/usr/bin/env python
"""Creates a pirx build file based on a Django settings file."""
import argparse
import imp
import inspect
import os
import pprint
import sys


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('in_path')
    parser.add_argument('out_path')
    args = parser.parse_args()

    in_path, out_path = args.in_path, args.out_path

    for path in [in_path, out_path]:
        if not os.path.exists(path):
            sys.stdout.write('File does not exist: %s\n' % path)
            sys.exit(1)

    mod = imp.load_source('settings', in_path)
    names = []
    for name, value in inspect.getmembers(mod):
        if name == name.upper():
            names.append(name)

    sys.stdout.write(', '.join(names) + '\n')
    while True:
        remove = raw_input('Press Enter or type name you want to remove: ')
        if remove:
            if remove in names:
                names.remove(remove)
                sys.stdout.write(', '.join(names) + '\n')
            else:
                sys.stdout.write('Name not in the list\n')
        else:
            break

    output = open(out_path, 'w')
    output.write('from pirx import Settings\n\n\n')
    output.write('settings = Settings()\n\n')
    for name in names:
        value = pprint.pformat(getattr(mod, name))
        output.write('settings.%s = %s\n' % (name.lower(), value))
    output.write('\nprint settings')

