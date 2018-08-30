# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.contrib.auth.decorators import login_required
from django.core import serializers
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from django.core.exceptions import MultipleObjectsReturned, ObjectDoesNotExist
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import redirect, render
from django.template import RequestContext, Template
from django.views.decorators.csrf import csrf_protect, csrf_exempt
from django.template.context_processors import csrf
from django.db import connection, transaction
from discordapp.models import *
import json


# render pages

# error page

@csrf_protect
def render_error_page(request):

    context = {}

    return render(request, 'error.html', context)

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
        "number_of_cards": 1,
    }

    return render(request, 'about_us.html', context)

@csrf_protect
def render_our_stuff(request):

    context = {
        "csrf": csrf,
        "text": "test text",
    }

    return redirect(request, 'our_stuff.html', context)

@csrf_protect
def render_bio(request):

    # if no member name is given from the request, return /about_us/
    if not request.GET:
        return redirect('about_us')

    context = {
        "csrf": csrf,
        "text": "test text",
    }

    return render(request, 'bio.html', context)


# access database