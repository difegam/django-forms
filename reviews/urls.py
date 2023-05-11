from django.urls import path

from . import views

app_name = "reviews"

urlpatterns = [
    path("", views.review, name="index"),
    path("thank-you", views.thank_you, name="thank-you-page"),
]
