from django.shortcuts import render
from django.http import JsonResponse
import pandas as pd


# Create your views here.
def index(request):
    return render(request, "index.html")


def employees(request):
    test = [{'name': 'John Adams'}]
    return JsonResponse(test, safe=False)
