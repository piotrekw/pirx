#!/usr/bin/env python
"""Creates a pirx build file based on a Django settings file."""
import argparse
import imp
import inspect
import os
import pprint
import sys


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('in_path')
    args = parser.parse_args()

    if not os.path.exists(args.in_path):
        sys.stderr.write('File does not exist: %s\n' % args.in_path)
        sys.exit(1)

    mod = imp.load_source('settings', args.in_path)
    names = []
    for name, value in inspect.getmembers(mod):
        if name == name.upper():
            names.append(name)

    sys.stderr.write(', '.join(names) + '\n')
    while True:
        sys.stderr.write('Press Enter or type name you want to remove: ')
        remove = raw_input()
        if remove:
            if remove in names:
                names.remove(remove)
                sys.stderr.write(', '.join(names) + '\n')
            else:
                sys.stderr.write('Name not in the list\n')
        else:
            break

    sys.stdout.write('from pirx import Settings\n\n\n')
    sys.stdout.write('settings = Settings()\n\n')
    for name in names:
        value = pprint.pformat(getattr(mod, name))
        sys.stdout.write('settings.%s = %s\n' % (name.lower(), value))
    sys.stdout.write('\nprint settings')

if __name__ == '__main__':
    main()
