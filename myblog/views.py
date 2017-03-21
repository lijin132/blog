import logging
from django.shortcuts import render
from django.template import loader, Context
from django.http import HttpResponse

logger = logging.getLogger('blog.views')
# Create your views here.
def index(request):
    t = loader.get_template("index.html")
    c = Context({})
    return HttpResponse(t.render(c))


def about(request):
    t = loader.get_template("about.html")
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
