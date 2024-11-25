from django import forms

from django_studybud.base.models import Room


class RoomForm(forms.ModelForm):
    class Meta:
        model = Room
        fields = "__all__"
        exclude = ("host", "participants")
