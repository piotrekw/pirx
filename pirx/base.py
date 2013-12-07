import collections
import datetime


class Settings(object):
    docstring = 'Settings built with Pirx on %(datetime)s'

    def __init__(self):
        self._settings = collections.OrderedDict()
        docstring = self.docstring % {
            'datetime': datetime.datetime.now()
            }
        self._set_raw_value('"""%s"""' % docstring)

    def __setattr__(self, name, value):
        if name.startswith('_'):
            super(Settings, self).__setattr__(name, value)
        else:
            self._settings[name] = value

    def __str__(self):
        lines = []
        for name, value in self._settings.iteritems():
            if name.startswith('_'):
                lines.append(value)
            else:
                lines.append('%s = %s' % (name.upper(), value.__repr__()))
        return '\n'.join(lines)

    def _set_raw_value(self, value):
        self._settings['_%d' % len(self._settings)] = value

    def imp(self, module_name):
        value = 'import %s' % module_name
        self._set_raw_value(value)

