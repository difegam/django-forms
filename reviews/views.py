from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse

from .forms import ReviewForm


# Create your views here.
def review(request):

    if request.method == "POST":

        #** Update operation using ModelForm
        #* existing_review = Review.objects.get(pk=1) # Get Obj
        #* form = ReviewForm(request.POST, instance=existing_review) # Populate with existing data

        form = ReviewForm(request.POST)
        if form.is_valid():
            #* Using form.Form
            # review_obj = Review(**form.cleaned_data)
            # review_obj.save()

            #* Using form.ModelForm
            form.save()
            return HttpResponseRedirect(reverse("reviews:thank-you-page"))
    else:
        form = ReviewForm()

    return render(request, template_name="reviews/review.html", context={"form": form})


def thank_you(request):
    return render(request, template_name="reviews/thank_you.html", context={})