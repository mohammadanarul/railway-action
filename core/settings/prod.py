from core.settings.base import *

# SECURITY WARNING: don't run with debug turned on in production!
SECRET_KEY = env("SECRET_KEY")
DEBUG = env("DEBUG")

ALLOWED_HOSTS = env("ALLOWED_HOSTS")

DATABASES = {
    "default": dj_database_url.config(default=env("DATABASE_URL"), conn_max_age=1800),
}

"""
the error solve.
Origin checking failed - https://web-production-acb7.up.railway.app does not match any trusted origins.
"""
CSRF_TRUSTED_ORIGINS = ["https://web-production-acb7.up.railway.app"]