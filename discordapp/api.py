# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.core import serializers
from django.core.exceptions import MultipleObjectsReturned, ObjectDoesNotExist
from django.db import connection, transaction
from discordapp.models import *
import json

def get_member_by_username(username):
    '''
    Function:
        Return a Member object based on a provided username.

    Params:
        - username (string): username of Member object to return.
    
    Return type(s):
        - Member object
        - None, if username parameter does not exist
    '''

    # get Member object from database, or return None if does not exist
    try:
        member = Member.objects.get(username=username)
    except ObjectDoesNotExist as odne:
        if str(odne) == "Member matching query does not exist.":
            member = None
        else:
            raise
    
    return member

def get_members(sort_by=None, amount=None):
    '''
    Function:
        Return a list of any number of Member objects optionally sorted.

    Params:
        -sort_by (str): column by which to sort the Member list.
        -amount (int): number of members to retrieve.
    
    Return type(s):
        List[Member object, ...]
    '''

    # if sort_by parameter is given, get sorted list of all Member objects
    if sort_by:
        try:
            getattr(Member, sort_by)
            members = Member.objects.order_by(sort_by)
        except AttributeError:
            members = Member.objects.all()
    # otherwise get all Member objects sorted by member_id
    else:
        members = Member.objects.all()
    
    # if specified amount, only include that number of Member objects
    if amount:
        members = members[:amount]

    return members


def get_social_media(member):
    ''' returns list of social media links for given Member object '''
    pass