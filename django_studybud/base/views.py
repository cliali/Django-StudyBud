from django.shortcuts import render

from .models import Room, Topic


# Create your views here.
def home(request):
    room = Room.objects.all()
    topics = Topic.objects.all()
    context = {"rooms": room, "topics": topics}
    return render(request, "base/home.html", context)


def room(request):
    context = {}
    return render(request, "base/room.html", context)
