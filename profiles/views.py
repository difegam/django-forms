from pathlib import Path

from django.core.files.uploadedfile import UploadedFile
from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.views import View

# Create your views here.


def store_file(file: UploadedFile):
    with Path("temp/image.jpg").open("wb+") as dest:
        for chunk in file.chunks():
            dest.write(chunk)


class CreateProfileView(View):

    def get(self, request):
        return render(request, "profiles/create_profile.html")

    def post(self, request):
        store_file(request.FILES["image"])
        return HttpResponseRedirect("/profiles")
