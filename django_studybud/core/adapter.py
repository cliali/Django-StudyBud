from allauth.account.adapter import DefaultAccountAdapter
from django.urls import reverse


class MyAccountAdapter(DefaultAccountAdapter):
    def get_login_redirect_url(self, request):
        return reverse("base:home")

    def get_logout_redirect_url(self, request):
        return reverse("base:home")

    def get_signup_redirect_url(self, request):
        return reverse("base:home")
