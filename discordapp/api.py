# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.core import serializers
from django.core.exceptions import MultipleObjectsReturned, ObjectDoesNotExist
from django.db import connection, transaction
from discordapp.models import *
import json

'''
This is the API for the SuperFam database.

About:
    - these API functions are to only be used by views.py.
    - these are the only functions allowed to access the database.

Summary:
    - get_member_by_username()
    - get_members()
    - get_pokemon_team_by_username()
    - get_social_media_by_username()
    - get_member_info()

TODO:
    Important:
        - Once we want to allow users to create accounts and comment around the website, we will need separate API functions for retrieving User objects.

    Optional:

Remember to cmd+f for TODO and NOTE.
'''


def get_member_by_username(username):
    '''
    Purpose:
        Return a Member object based on a provided username.

    Params:
        - username (string): username of Member object to return.

    Return values:
        Intended:
            - Member object
        Erroneous:
            - ValueError: username parameter does not exist.
            - Other Error:
                - unexpected error occured querying the Member object.
    
    Function:
        Step 1.
            - validate username parameter.
        Step 2.
            - get Member object from database, or return None if does not exist.
    
    TODO
        Optional:
            - make this function flexible by making username optional and adding more optional parameters. This should probably entail changing the function name; something like get_member_by_attribute().
    '''

    # Step 1. validate username parameter.
    # NOTE - Since wrappers for this function may receive Member objects as their username parameter, validation for the Member type will go here.
    if type(username) == Member:
        username = username.username
    else:
        try:
            # NOTE - Member.username is of the unicode type.
            assert(isinstance(username, unicode) or isinstance(username, str))
        except AssertionError:
            raise TypeError("get_member_by_username() must only take a string or unicode object. Given input was of type {}.".format(type(username)))


    # Step 2. get Member object from database, or return None if does not exist.
    try:
        member = Member.objects.get(username=username)
    except ObjectDoesNotExist as odne:
        if str(odne) == "Member matching query does not exist.":
            raise ValueError(
                "User does not exist with username {}.".format(username)
            )
        else:
            raise
    
    return member


def get_members(sort_by="member_id", amount=None):
    '''
    Purpose:
        Return a list of any number of Member objects sorted by member_id or by another column.

    Params:
        - sort_by (str): column by which to sort the Member list. Defaults to primary key "member_id".
        - amount (int): number of members to retrieve.

    Return values:
        Intended:
            - List[Member] object
    
    Function:
        Step 1.
            - query for all Members sorted by the given sort_by parameter.
        Step 2.
            - filter the queryset to the number given by the amount parameter.
    
    TODO
        Optional:
            - account for a change in the name of the member_id attribute of the Member class. Currently that column name is hardcoded. To account for a possible change, we must either throw an error or return a default value after determining that the query is failing on sorting by member_id.
    '''

    # Step 1. create a list of all Members sorted by the given sort_by attribute.
    try:
        getattr(Member, sort_by)
        members = Member.objects.order_by(sort_by)
    except AttributeError:
        members = get_members(sort_by="member_id")

    # Step 2. filter the list down to the number of the given amount attribute.
    if amount:
        members = members[:amount]

    return members


def get_pokemon_team_by_username(username):
    '''
    Purpose:
        Returns LinkMemberPokemon object associated with a given username.
    
    Params:
        - username (str): username of Member object whose LinkMemberPokemon object to return.

    Return values:
        Intended:
            - LinkMemberPokemon object
            - None: LinkMemberPokemon object does not exist with given member_id.
        Erroneous:
            - ValueError: Member does not exist with given username. See get_member_by_username() for details.
            - Other Error:
                - unexpected error occured querying the LinkMemberPokemon object.
    
    Function:
        Step 1.
            - call get_member_by_username() on the given username parameter.
        Step 2.
            - query for LinkMemberPokemon object whose member_id matches that of the Member objects.

    TODO:
    
    '''

    # Step 1. call get_member_by_username() on the given username parameter.
    member = get_member_by_username(username)
    
    # Step 2. query for LinkMemberPokemon object whose member_id matches that of the Member objects.
    try:
        member_pokemon = LinkMemberPokemon.objects.get(
            member_id=member.member_id
        )
    except ObjectDoesNotExist as odne:
        member_pokemon = None
    except Exception:
        raise
    
    return member_pokemon


def get_social_media_by_username(username):
    '''
    Purpose:
        Return LinkMemberSocialMedia object associated with a given username.

    Params:
        - username (String):
            - username of Member object whose LinkMemberSocialMedia object to return.

    Return values:
        Intended:
            - LinkMemberSocialMedia object
            - None: LinkMemberSocialMedia object does not exist with given member_id.
        Erroneous:
            - ValueError: Member does not exist with given username. See get_member_by_username() for details.
            - Other Error:
                - unexpected error occured querying the LinkMemberSocialMedia object.
    
    Function:
        Step 1.
            - call get_member_by_username() on the given username parameter.
        Step 2.
            - query for LinkMemberSocialMedia object whose member_id matches that of the Member objects.

    TODO:
    
    '''

    # Step 1. call get_member_by_username() on the given username parameter.
    member = get_member_by_username(username)

    # Step 2. query for LinkMemberSocialMedia object whose member_id matches that of the Member objects.
    try:
        member_social_media = LinkMemberSocialMedia.objects.get(
            member_id=member.member_id
        )
    except AttributeError as ae:
        if str(ae) == "'NoneType' object has no attribute 'social_media_id'":
            member_social_media = None
        else:
            raise

    return member_social_media


def get_member_info(username, info_type):
    '''
    Purpose:
        Returns a members associated LinkMemberPokemon or LinkMemberSocialMedia object.
    
    Params:
        - username (String/Member):
            - username of Member object whose LinkMemberPokemon or LinkMemberSocialMedia object to return.
            - also takes Member objects.
        - info_type (String):
            - name of table whose data should be pulled.
            - should only be "LinkMemberPokemon" or "LinkMemberSocialMedia".

    Return values:
        Intended:
            - LinkMemberPokemon object: see get_pokemon_team_by_username()
            - LinkMemberSocialMedia object: see get_social_media_by_username()
            - None: user has no data in the table referenced by the given info_type parameter.
        Erroneous:
            - ValueError:
                - this function is not handling the info_type value.

    Function:
        Step 1.
            - call the appropriate function based on the info_type parameter.
    TODO:
        - standardize available info_type inputs with either the database table names or the model names. "pokemon" and "social_media" Currently don't align with either.
    '''

    # Step 1. call the appropriate function based on the info_type parameter.
    if info_type == "pokemon":
        member_info_link = get_pokemon_team_by_username(username)
    elif info_type == "social_media":
        member_info_link = get_social_media_by_username(username)
    else:
        raise ValueError(
            "get_member_info() has not been modified to retrieve values for info_type {}.".format(info_type)
        )

    return member_info_link