from django.shortcuts import render
from django.http import HttpResponse

from .models import *

#Catalogue Page
def catalogue_view(request, *args, **kwargs):
    return render(request, "home.html", {})

    