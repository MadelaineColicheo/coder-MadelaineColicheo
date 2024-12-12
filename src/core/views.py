from django.shortcuts import render
from django.http import HttpResponse


def index(request):
     context = {"año":2024}
     return render(request, "core/index.html", context)