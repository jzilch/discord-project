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
from discordapp.api import *
import json


@csrf_protect
def render_homepage(request):

    context = {
        "csrf": csrf,
    }

    return render(request, 'index.html', context)

@csrf_protect
def render_about(request):

    members = get_members()

    # gather data to send to about.html
    context = {
        "csrf": csrf,
        "members": members
    }

    return render(request, 'about.html', context)

@csrf_protect
def render_about_member(request, member_name):

    # ensure given member username exists in the database
    try:
        member = get_member_by_username(member_name)
    except ValueError as ve:
        return redirect('about')

    # gather data to send to about_member.html
    context = {
        "csrf": csrf,
        "member": member,
    }

    return render(request, 'about_member.html', context)

@csrf_protect
def render_our_stuff(request):

    context = {
        "csrf": csrf,
    }

    return render(request, 'our_stuff.html', context)