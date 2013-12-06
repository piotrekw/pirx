class Settings(object):
    def __init__(self):
        self._settings = {}

    def __setattr__(self, name, value):
        if name.startswith('_'):
            super(Settings, self).__setattr__(name, value)
        else:
            self._settings[name] = value

    def write(self):
        for name, value in self._settings.iteritems():
            print '%s = %s' % (name.upper(), value.__repr__())

