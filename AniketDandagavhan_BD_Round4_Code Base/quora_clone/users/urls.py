from django.urls import path
from users import views

urlpatterns = [
    path("follow/",views.UserFollow.as_view()),
]