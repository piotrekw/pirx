import collections


class Settings(object):
    def __init__(self):
        self._settings = collections.OrderedDict()

    def __setattr__(self, name, value):
        if name.startswith('_'):
            super(Settings, self).__setattr__(name, value)
        else:
            self._settings[name] = value

    def _set_raw_value(self, value):
        self._settings['_%d' % len(self._settings)] = value

    def write(self):
        for name, value in self._settings.iteritems():
            if name.startswith('_'):
                print value
            else:
                print '%s = %s' % (name.upper(), value.__repr__())

