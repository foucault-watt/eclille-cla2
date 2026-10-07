from .base import *

# Debug
DEBUG = False


# Email

EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
EMAIL_HOST = config("EMAIL_HOST")
EMAIL_HOST_FROM = config("EMAIL_FROM")
EMAIL_HOST_USER = config("EMAIL_LOGIN")
EMAIL_HOST_PASSWORD = config("EMAIL_PASSWORD")
EMAIL_PORT = 465
EMAIL_USE_SSL = True


# Database
# https://docs.djangoproject.com/en/3.1/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'OPTIONS': {
            'host': config("DATABASE_HOST", "127.0.0.1"),
            'port': int(config("DATABASE_PORT", "3306")),
            'user': config("DATABASE_USER"),
            'passwd': config("DATABASE_PASSWORD"),
            'db': config("DATABASE_NAME"),
        },
    }
}


# Password validation
# https://docs.djangoproject.com/en/3.1/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]


# Logging

#LOGGING = {
#    'version': 1,
#    'disable_existing_loggers': False,
#    'handlers': {
#        'mail_admins': {
#            'level': 'ERROR',
#            'class': 'django.utils.log.AdminEmailHandler',
#            'include_html': True,
#        }
#    },
#    'loggers': {
#        'django': {
#            'level': 'ERROR',
#            'handlers': ['mail_admins'],
#        }
#    }
#}


# Derrière le reverse proxy Coolify (Traefik) : TLS terminé par le proxy

SECURE_PROXY_SSL_HEADER = ("HTTP_X_FORWARDED_PROTO", "https")
SESSION_COOKIE_SECURE = config("SECURE_COOKIES", True, cast=bool)
CSRF_COOKIE_SECURE = config("SECURE_COOKIES", True, cast=bool)


# Fichiers statiques servis par WhiteNoise (plus d'Apache devant)

MIDDLEWARE.insert(
    MIDDLEWARE.index("django.middleware.security.SecurityMiddleware") + 1,
    "whitenoise.middleware.WhiteNoiseMiddleware",
)
STATICFILES_STORAGE = "whitenoise.storage.CompressedStaticFilesStorage"


# Médias (uploads) : Django les sert lui-même seulement si SERVE_MEDIA=true.
# À activer uniquement si l'ancien Apache les exposait déjà (cf. urls.py).

SERVE_MEDIA = config("SERVE_MEDIA", False, cast=bool)
