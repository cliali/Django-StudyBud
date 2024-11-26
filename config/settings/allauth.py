from config.django import base

base.MIDDLEWARE += [
    "allauth.account.middleware.AccountMiddleware",
]
base.AUTHENTICATION_BACKENDS += [
    "django.contrib.auth.backends.ModelBackend",
    "allauth.account.auth_backends.AuthenticationBackend",
]

ACCOUNT_ADAPTER = "django_studybud.core.adapter.MyAccountAdapter"

ACCOUNT_AUTHENTICATION_METHOD = "email"
ACCOUNT_EMAIL_REQUIRED = True
