from typing import Any

from django.http import HttpResponseRedirect
from django.shortcuts import get_object_or_404, render
from django.urls import reverse
from django.views import View
from django.views.generic.base import TemplateView

from .forms import ReviewForm
from .models import Review


# DJango Class base views
# https://docs.djangoproject.com/en/4.2/topics/class-based-views/
class ReviewView(View):

    def get(self, request):
        form = ReviewForm()
        return self.render_view(request, form)

    def post(self, request):
        form = ReviewForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse("reviews:thank-you-page"))
        return self.render_view(request, form)

    def render_view(self, request, form):
        return render(request, template_name="reviews/review.html", context={"form": form})


# class ThankYouView(View):
#     def get(self, request, *args, **kwargs):
#         return render(request, template_name="reviews/thank_you.html", context={})


class ThankYouView(TemplateView):
    template_name = "reviews/thank_you.html"

    def get_context_data(self, **kwargs: Any) -> dict[str, Any]:
        context = super().get_context_data(**kwargs)
        context["message"] = "This Works!"
        return context


class ReviewListView(TemplateView):
    template_name = "reviews/review_list.html"

    def get_context_data(self, **kwargs: Any) -> dict[str, Any]:
        context = super().get_context_data(**kwargs)
        context["reviews"] = Review.objects.all()
        return context


class SingleReviewView(TemplateView):
    template_name = "reviews/review_detail.html"

    def get_context_data(self, **kwargs: Any) -> dict[str, Any]:
        context = super().get_context_data(**kwargs)
        review_id = kwargs.get("id", 0)
        context["review"] = get_object_or_404(Review, pk=review_id)
        return context