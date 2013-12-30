import os


def path(*p):
    """Return full path of a directory inside project's root"""
    import __main__
    project_root = os.path.dirname(os.path.realpath(__main__.__file__))
    return os.path.join(project_root, *p)

