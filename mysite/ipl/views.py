from django.shortcuts import render
from django.http import HttpResponse
from .models import match
from django.db.models import Count
# Create your views here.
def index(request):
    return render(request, "ipl/index.html", {})

def js(request):
    return render(request, "ipl/js.html", {})


def match_details(request):
    obj = match.objects.values('winner').order_by().annotate(Count('winner'))
    x = match.objects.values('season').order_by().annotate(Count('venue'))
    context = {
        "object": obj,
        "X": x,
    }
    return render(request, "ipl/match_details.html", context)
