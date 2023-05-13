from typing import Any

from django.db.models.query import QuerySet
from django.urls import reverse_lazy
from django.views.generic import (CreateView, DeleteView, DetailView, ListView, UpdateView)
from django.views.generic.base import TemplateView

from .forms import ReviewForm
from .models import Review


# DJango Class base views
# https://docs.djangoproject.com/en/4.2/topics/class-based-views/
class ReviewView(CreateView):
    model = Review
    form_class = ReviewForm
    template_name = "reviews/review.html"
    success_url = reverse_lazy("reviews:thank-you-page")

    # # FormView
    # def form_valid(self, form: Any) -> HttpResponse:
    #     form.save()
    #     return super().form_valid(form)


#     view
#     def get(self, request):
#         form = ReviewForm()
#         return self.render_view(request, form)

#     def post(self, request):
#         form = ReviewForm(request.POST)
#         if form.is_valid():
#             form.save()
#             return HttpResponseRedirect(reverse("reviews:thank-you-page"))
#         return self.render_view(request, form)

#     def render_view(self, request, form):
#         return render(request, template_name="reviews/review.html", context={"form": form})

# class ThankYouView(View):
#     def get(self, request, *args, **kwargs):
#         return render(request, template_name="reviews/thank_you.html", context={})


class ReviewUpdateView(UpdateView):
    model = Review
    form_class = ReviewForm
    template_name = "reviews/review.html"
    success_url = reverse_lazy("reviews:thank-you-page")
    template_name_suffix = "_update_form"


class ReviewDeleteView(DeleteView):
    model = Review
    success_url = reverse_lazy("reviews:reviews")


class ThankYouView(TemplateView):
    template_name = "reviews/thank_you.html"

    def get_context_data(self, **kwargs: Any) -> dict[str, Any]:
        context = super().get_context_data(**kwargs)
        context["message"] = "This Works!"
        return context


class ReviewListView(ListView):
    template_name = "reviews/review_list.html"
    model = Review
    context_object_name = "reviews"

    def get_queryset(self) -> QuerySet[Any]:
        base_query = super().get_queryset()
        return base_query.filter(rating__gt=0)


class ReviewDetailView(DetailView):
    template_name = "reviews/review_detail.html"
    model = Review