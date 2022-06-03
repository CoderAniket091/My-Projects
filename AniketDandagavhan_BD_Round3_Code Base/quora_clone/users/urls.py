from django.urls import path
from users import views

urlpatterns = [
    path("listUsers/<id>/",views.listUsers.as_view()),
    path("addFollower/<id>/",views.AddFollower.as_view()),
]