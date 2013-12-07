pirx
====

Pirx is the first tool that lets you build Django settings files tailored to
your needs. The age of ``local_settings`` has just ended. Because the best
``settings.py`` is no ``settings.py``!

Why
---

Pirx will make your life easier and your project cleaner, because:

* it lets you separate settings-building logic from settings file itself
* it makes debugging easier, as you can check the final settings values
  __before__ running your application
* finally you can easily keep any credentials away from code repository
* it provides stuff that you always use while writing settings (e.g.
  PROJECT\_ROOT path)
