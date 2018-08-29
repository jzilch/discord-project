# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.contrib.auth.decorators import login_required
from django.core import serializers
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from django.core.exceptions import MultipleObjectsReturned, ObjectDoesNotExist
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from django.template import RequestContext, Template
from django.views.decorators.csrf import csrf_protect, csrf_exempt
from django.template.context_processors import csrf
from django.db import connection, transaction
from discordapp.models import *
import json


# render pages

@csrf_protect
def render_homepage(request):

    context = {
        "csrf": csrf,
        "text": "test text",
    }

    return render(request, 'index.html', context)

@csrf_protect
def render_about_us(request):
    
    context = {
        "csrf": csrf,
        "text": "test text",
    }

    return render(request, 'about_us.html', context)

@csrf_protect
def render_our_stuff(request):

    context = {
        "csrf": csrf,
        "text": "test text",
    }

    return render(request, 'our_stuff.html', context)


# access database