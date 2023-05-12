from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse

from .forms import ReviewForm
from .models import Review


# Create your views here.
def review(request):

    if request.method == "POST":
        form = ReviewForm(request.POST)
        if form.is_valid():
            print(type(form.cleaned_data), form.cleaned_data)
            review_obj = Review(**form.cleaned_data)
            print(review_obj)
            review_obj.save()
            return HttpResponseRedirect(reverse("reviews:thank-you-page"))
    else:
        form = ReviewForm()

    return render(request, template_name="reviews/review.html", context={"form": form})


def thank_you(request):
    return render(request, template_name="reviews/thank_you.html", context={})