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
def render_coming_soon(request):

    context = {}

    return render(request, 'coming_soon.html', context)

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

    # retrieve PokemonTeam and SocialMedia objects for member
    pokemon_team_link = get_member_info(member.username, "pokemon_team")
    social_media_link = get_member_info(member.username, "social_media")

    # gather data to send to about_member.html
    context = {
        "csrf": csrf,
        "member": member,
        "pokemon_team": pokemon_team_link,
        "social_media": social_media_link
    }

    return render(request, 'about_member.html', context)

@csrf_protect
def render_our_stuff(request):

    context = {
        "csrf": csrf,
    }

    return render(request, 'our_stuff.html', context)