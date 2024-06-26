from .base import *

#SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = "django-insecure-+3ai*)u)0yxpvfa9g=yg(os9c$)g6l64$en0vpf5*eqxm908w3"

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = []

DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.sqlite3",
        "NAME": BASE_DIR / "db.sqlite3",
    }
}