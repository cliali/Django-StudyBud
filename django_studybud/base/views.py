from django.contrib.auth.decorators import login_required
from django.db.models import Q
from django.http import HttpResponse
from django.shortcuts import redirect, render

from django_studybud.base.forms import RoomForm

from .models import Message, Room, Topic


# Create your views here.
def home(request):
    q = request.GET.get("q") if request.GET.get("q") is not None else ""

    rooms = Room.objects.filter(
        Q(topic__name__icontains=q) | Q(name__icontains=q) | Q(description__icontains=q)
    )
    topics = Topic.objects.all()
    room_count = rooms.count()
    context = {"rooms": rooms, "topics": topics, "room_count": room_count}
    return render(request, "base/home.html", context)


def room(request, pk):
    room = Room.objects.get(id=pk)
    room_messages = Message.objects.filter(room=room).order_by("-created")
    participants = room.participants.all()

    if request.method == "POST":
        Message.objects.create(
            user=request.user, room=room, body=request.POST.get("body")
        )
        room.participants.add(request.user)
        return redirect("base:room", pk=room.id)

    context = {
        "room": room,
        "participants": participants,
        "room_messages": room_messages,
    }
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


@login_required
def update_room(request, pk):
    room = Room.objects.get(id=pk)
    form = RoomForm(instance=room)
    if request.user != room.host:
        return HttpResponse("You are not allowed here!!")

    if request.method == "POST":
        form = RoomForm(request.POST, instance=room)
        if form.is_valid():
            form.save()
            return redirect("base:home")
    context = {"form": form, "room": room}
    return render(request, "base/update-room.html", context)


@login_required
def delete_room(request, pk):
    room = Room.objects.get(id=pk)
    if request.user != room.host:
        return HttpResponse("You are not allowed here!!")

    if request.method == "POST":
        room.delete()
        return redirect("base:home")

    return render(request, "base/delete-room.html", {"obj": room})
