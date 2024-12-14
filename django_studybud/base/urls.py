from django.urls import path

from . import views

app_name = "base"
urlpatterns = [
    path("", views.home, name="home"),
    path("room/<int:pk>/", views.room, name="room"),
    path("profile/update/", views.update_user, name="update-user"),
    path("profile/<str:pk>/", views.user_profile, name="user-profile"),
    path("create-room/", views.create_room, name="create-room"),
    path("update-room/<int:pk>/", views.update_room, name="update-room"),
    path("delete-room/<int:pk>/", views.delete_room, name="delete-room"),
    path("delete-message/<int:pk>/", views.delete_message, name="delete-message"),
]
