from django.shortcuts import render
from django.http import JsonResponse
from django.conf import settings


# Create your views here.
def index(request):
    return render(request, "index.html")


def employees(request):
    data = settings.DATAFRAME
    all_employees = data.to_dict(orient='records')
    return JsonResponse(all_employees, safe=False)
