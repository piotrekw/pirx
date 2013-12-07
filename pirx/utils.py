import os


def setting(name):
    return name.upper()

def path(*p):
    import __main__
    project_root = os.path.dirname(os.path.realpath(__main__.__file__))
    return os.path.join(project_root, *p)

