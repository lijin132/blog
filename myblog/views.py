from django.shortcuts import render
from django.template import loader, Context
from django.http import HttpResponse


# Create your views here.
def index(request):
    t = loader.get_template("index.html")
    c = Context({})
    return HttpResponse(t.render(c))


def single(request):
    t = loader.get_template("single.html")
    c = Context({})
    return HttpResponse(t.render(c))


def archive(request):
    t = loader.get_template("archive.html")
    c = Context({})
    return HttpResponse(t.render(c))


def contact(request):
    t = loader.get_template("contact.html")
    c = Context({})
    return HttpResponse(t.render(c))
