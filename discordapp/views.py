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

    members = Member.objects.all()
    
    context = {
        "csrf": csrf,
        "text": "test text",
        "members": members
    }

    return render(request, 'about_us.html', context)

@csrf_protect
def render_about_member(request, member_name):

    # TODO: this is a temporary measure.
    # In prod, this will assert that member_name is in the db
    # or else reroute to /about/
    members = [
        'squideon',
        'stringer',
        'bellydrum',
        'wacky280',
        'kennzoil',
    ]
    if member_name not in members:
        return redirect('about_us')


    # gather data to send to about_member page
    context = {
        "csrf": csrf,
        "text": "test text",
        "member_name": member_name,
    }

    return render(request, 'about_member.html', context)

@csrf_protect
def render_our_stuff(request):

    context = {
        "csrf": csrf,
        "text": "test text",
    }

    return render(request, 'our_stuff.html', context)


# access database