from pirx import Settings, path, arg


settings = Settings()

settings.static_root = path('static/')
settings.media_root = path('media/') if arg('debug') else '/var/media/'

print settings
