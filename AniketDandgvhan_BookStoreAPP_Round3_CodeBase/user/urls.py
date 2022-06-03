from django.urls import path
from user import views

urlpatterns = [
    path("cart/",views.BooksCart.as_view()),
    path("cart/<id>/",views.GetCart.as_view()),
]
