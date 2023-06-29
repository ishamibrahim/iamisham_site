from django.shortcuts import render

from iamisham_site.settings import STATIC_URL
from django.template import loader
from django.http import HttpResponse


# Create your views here.
def index(request):
    template = loader.get_template("iamisham_app/index.html")
    context = {
        "STATIC_URL": STATIC_URL
    }

    return HttpResponse(template.render(context, request))


