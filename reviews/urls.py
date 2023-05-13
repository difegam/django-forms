from django.urls import path

from . import views

app_name = "reviews"

urlpatterns = [
    path("", views.ReviewView.as_view(), name="index"),
    # path("", views.review, name="index"),
    path("thank-you", views.ThankYouView.as_view(), name="thank-you-page"),
    path("reviews", views.ReviewListView.as_view(), name="reviews"),
    path("reviews/<int:pk>", views.ReviewDetailView.as_view(), name="review-detail"),
]
