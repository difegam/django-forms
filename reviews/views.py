from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse
from django.views import View

from .forms import ReviewForm


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

# django function based views
# https://docs.djangoproject.com/en/4.1/topics/http/views/
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