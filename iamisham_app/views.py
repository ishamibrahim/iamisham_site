from django.db.models import Q
from django.shortcuts import render
from rest_framework.decorators import action
from rest_framework.generics import get_object_or_404
from rest_framework.permissions import IsAuthenticated
from rest_framework_simplejwt.authentication import JWTAuthentication

from iamisham_site.settings import STATIC_URL
from django.template import loader
from django.http import HttpResponse
from rest_framework import status


# Create your views here.
def index(request):
    template = loader.get_template("iamisham_app/index.html")
    context = {
        "STATIC_URL": STATIC_URL
    }

    return HttpResponse(template.render(context, request))
