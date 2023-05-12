from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse

from .forms import ReviewForm


# Create your views here.
def review(request):

    if request.method == "POST":
        form = ReviewForm(request.POST)
        if form.is_valid():
            print(form.cleaned_data)
            return HttpResponseRedirect(reverse("reviews:thank-you-page"))
    else:
        form = ReviewForm()

    return render(request, template_name="reviews/review.html", context={"form": form})


def thank_you(request):
    return render(request, template_name="reviews/thank_you.html", context={})