from django import forms

from django_studybud.base.models import Room
from django_studybud.core.models import User


class RoomForm(forms.ModelForm):
    class Meta:
        model = Room
        fields = "__all__"
        exclude = ("host", "participants")


class UserForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ["username", "first_name", "last_name", "email", "bio"]
