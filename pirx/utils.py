import os


def setting(name):
    return name.upper()

def path(subpath):
    project_root = os.path.dirname(os.path.realpath(__file__))
    return os.path.join(project_root, subpath)

