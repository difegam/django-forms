from django.shortcuts import render


# Create your views here.
def review(request):
    return render(request, template_name="reviews/review.html", context={})