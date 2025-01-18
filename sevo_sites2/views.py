from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse

from .models import Site2

# Create your views here.

def index(request):
    return HttpResponse("sevo_sites2::index")


def homepage(request):
    site = get_object_or_404(Site2, is_home=True)
    
    return render(request, "sevo_sites2/detail.html", {
        "site": site
    })


def detail(request, slug):
    site = get_object_or_404(Site2, slug=slug)
    if site == Site2.get_home_page():
        return redirect("index")
    print("path: ", request.path)
    return render(request, "sevo_sites2/detail.html", {
        "site": site,
    })
