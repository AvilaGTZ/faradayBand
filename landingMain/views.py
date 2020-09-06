from django.shortcuts import render, redirect
from django.core.exceptions import ObjectDoesNotExist
from .models import *


def Home(request):
    return render(request, 'index.html')
