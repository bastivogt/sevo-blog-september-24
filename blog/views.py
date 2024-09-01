from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse

from . import models

# Create your views here.

def redirect(request):
    url = reverse("blog-index")
    return HttpResponseRedirect(url)


def all(request):
    posts = models.Post.objects.filter(published=True)
    return render(request, "blog/all.html", {
        "title": "All",
        "posts": posts
    })

def index(request):
    posts = models.Post.objects.filter(published=True, featured=True)
    return render(request, "blog/index.html", {
        "title": "Index",
        "posts": posts
    })

