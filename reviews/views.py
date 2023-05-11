from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse


# Create your views here.
def review(request):

    if request.method == "POST":
        entered_username = request.POST["username"]
        print(entered_username)
        return HttpResponseRedirect(reverse("reviews:thank-you-page"))

    return render(request, template_name="reviews/review.html", context={})


def thank_you(request):
    return render(request, template_name="reviews/thank_you.html", context={})