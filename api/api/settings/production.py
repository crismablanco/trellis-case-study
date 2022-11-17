from .base import *

DEBUG = False
DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.postgresql",
        "ATOMIC_REQUESTS": True,
        "USER": os.getenv("POSTGRESQL_USER", "postgres"),
        "PASSWORD": os.getenv("POSTGRESQL_PASSWORD", "postgres"),
        "NAME": os.getenv("POSTGRESQL_DB_NAME", "trellis_api_db"),
        "HOST": os.getenv("POSTGRESQL_HOST", "127.0.0.1"),
        "PORT": os.getenv("POSTGRESQL_PORT", "5432"),
    }
}
