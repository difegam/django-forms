from django.urls import path

from . import views

app_name = "reviews"

urlpatterns = [
    path("", views.ReviewView.as_view(), name="index"),
    # path("", views.review, name="index"),
    path("thank-you", views.ThankYouView.as_view(), name="thank-you-page"),
    path("reviews", views.ReviewListView.as_view(), name="reviews"),
    path("reviews/<int:pk>", views.ReviewDetailView.as_view(), name="review-detail"),
    path("reviews/<int:pk>/update", views.ReviewUpdateView.as_view(), name="review-update"),
    path("reviews/<int:pk>/delete", views.ReviewDeleteView.as_view(), name="review-delete"),
]
