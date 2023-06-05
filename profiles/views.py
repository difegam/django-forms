from pathlib import Path

from django.core.files.uploadedfile import UploadedFile
from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.views import View

from .forms import ProfileForm

# Create your views here.


def store_file(file: UploadedFile):
    with Path("temp/image.jpg").open("wb+") as dest:
        for chunk in file.chunks():
            dest.write(chunk)


class CreateProfileView(View):

    def get(self, request):
        form = ProfileForm()
        return render(request, "profiles/create_profile.html", context={"form": form})

    def post(self, request):
        submitted_form = ProfileForm()

        if submitted_form.is_valid():
            store_file(request.FILES["image"])
            return HttpResponseRedirect("/profiles")

        return render(request, "profiles/create_profile.html", context={"form": submitted_form})
