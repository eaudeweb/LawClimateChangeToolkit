import environ

root = environ.Path(__file__) - 2
env = environ.Env(DEBUG=(bool, False),)

BASE_DIR = root()

SECRET_KEY = env('SECRET_KEY', default='secret')
DEBUG = env('DEBUG')

DATABASES = {
    'default': env.db(default='sqlite:////tmp/my-tmp-sqlite.db'),
}

ALLOWED_HOSTS = env.list('ALLOWED_HOSTS', default=['*'])

STATIC_URL = '/static/'
STATIC_ROOT = '/var/www/'

STATICFILES_DIRS = [
    root.path('static/')()
]

MEDIA_URL = '/files/'
MEDIA_ROOT = root.path('media/uploadfiles/')()

# sentry configuration
SENTRY_PUBLIC_DSN = env('SENTRY_PUBLIC_DSN', default='')
SENTRY_DSN = env('SENTRY_DSN', default='')

if not DEBUG and SENTRY_DSN:
    RAVEN_CONFIG = {'dsn': SENTRY_DSN}