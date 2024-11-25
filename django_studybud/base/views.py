from django.contrib.auth.decorators import login_required
from django.shortcuts import redirect, render

from django_studybud.base.forms import RoomForm

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


@login_required
def create_room(request):
    form = RoomForm()
    topics = Topic.objects.all()
    if request.method == "POST":
        topic_name = request.POST.get("topic")
        topic, created = Topic.objects.get_or_create(name=topic_name)

        Room.objects.create(
            host=request.user,
            topic=topic,
            name=request.POST.get("name"),
            description=request.POST.get("description"),
        )
        return redirect("base:home")
    context = {"form": form, "topics": topics}
    return render(request, "base/room_form.html", context)
