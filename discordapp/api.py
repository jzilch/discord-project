# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.core import serializers
from django.core.exceptions import MultipleObjectsReturned, ObjectDoesNotExist
from django.db import connection, transaction
from discordapp.models import *
import json

'''
This is the API for the SuperFam website.

About:
    - these functions are to only be used by views.py.
    - these functions are the only functions allowed to access the database.

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
            - query the database for a Member with the given username, returning None if the username is not found.
    
    TODO
        Optional:
            - make this function flexible by making username optional and adding more optional parameters. This should probably entail changing the function name; something like get_member_by_attribute().
    '''

    # Step 1. get Member object from database, or return None if does not exist
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


def get_members(sort_by=None, amount=None):
    '''
    Purpose:
        Return a list of any number of Member objects optionally sorted.

    Params:
        - sort_by (str): column by which to sort the Member list.
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
    if sort_by:
        try:
            getattr(Member, sort_by)
            members = Member.objects.order_by(sort_by)
        except AttributeError:
            members = get_members(sort_by="member_id")
    else:
        members = get_members(sort_by="member_id")
    
    # Step 2. filter the list down to the number of the given amount attribute.
    if amount:
        members = members[:amount]

    return members


def get_pokemon_team_by_username(username):
    '''
    Purpose:
        Returns PokemonTeam object associated with a given username.
    
    Params:
        - username (str): username of Member object whose PokemonTeam object to return.

    Return values:
        Intended:
            - PokemonTeam object
            - None: Member's pokemon_team_id is blank or Null.
        Erroneous:
            - ValueError: see get_member_by_username()
            - Other Error:
                - unexpected error occured querying the PokemonTeam object.
    
    Function:
        Step 1.
            - call get_member_by_username() on the given username parameter.
        Step 2.
            - query for PokemonTeam object whose pokemon_team_id matches that of the Member object.

    TODO:
    
    '''

    # Step 1. call get_member_by_username() on the given username parameter.
    member = get_member_by_username(username)
    
    # Step 2. query for PokemonTeam object whose pokemon_team_id matches that of the Member object.
    try:
        pokemon_team_link = PokemonTeam.objects.get(
            pokemon_team_id=member.pokemon_team_id.pokemon_team_id
        )
    except AttributeError as ae:
        if str(ae) == "'NoneType' object has no attribute 'pokemon_team_id'":
            pokemon_team_link = None
        else:
            raise
    
    return pokemon_team_link


def get_social_media_by_username(username):
    '''
    Purpose:
        Return SocialMedia object associated with a given username.

    Params:
        - username (str): username of Member object whose SocialMedia object to return.

    Return values:
        Intended:
            - SocialMedia object
            - None: Member's social_media_id is blank or Null.
        Erroneous:
            - ValueError: user does not exist with given username parameter.
    
    Function:
        Step 1.
            - call get_member_by_username() on the given username parameter.
        Step 2.
            - if Member does not exist with given username, return ValueError.
        Step 3.
            - query for SocialMedia object whose social_media_id matches that of the Member object.

    TODO:
    
    '''

    # Step 1. call get_member_by_username() on the given username parameter.
    member = get_member_by_username(username)

    # Step 2. if Member does not exist with given username, return ValueError.
    if not member:
        raise ValueError("User does not exist with that username.", username)
    
    # Step 3. query for SocialMedia object whose social_media_id matches that of the Member object.
    try:
        social_media_link = SocialMedia.objects.get(
            social_media_id=member.social_media_id.social_media_id
        )
    except AttributeError as ae:
        if str(ae) == "'NoneType' object has no attribute 'social_media_id'":
            social_media_link = None

    return social_media_link


def get_member_info(username, info_type):
    '''
    Purpose:
        Returns a Members PokemonTeam or SocialMedia object.
    
    Params:
        - username (str): username of Member object whose PokemonTeam object to return.
        - info_type (str): Member ForeignKey to query (should only be "PokemonTeam" or "SocialMedia")

    Return values:
        Intended:
            - PokemonTeam object: see get_pokemon_team_by_username()
            - SocialMedia object: see get_social_media_by_username()
            - None: user has no data for given info_type parameter.
        Erroneous:
            - AttributeError:
                - info_type parameter is erroneous. ForeignKey of name given by info_type parameter does not exist on Member object. See error message for details.
            - ValueError:
                - username parameter is erroneous. Member object does not exist with given username. See error message for details.
            - ValueError:
                - this function is not handling a new info_type value. ForeignKey of name given by info_type parameter DOES exist on Member object, but this function has not yet been modified to be able to retrieve it. See error message for details.

    Function:
        Step 1.
            - validate info_type parameter. Return ValueError if given info_type is not an existing ForeignKey on the Member class.
        Step 2.
    TODO:
    
    '''

    # Step 1. validate info_type parameter.
    try:
        getattr(Member, info_type + "_id")
    except AttributeError:
        raise AttributeError(
            "ForeignKey of name \"{}\" does not exist on Member object.\nOptions are:\n-\"pokemon_team\"\n-\"social_media\"".format(info_type)
        )
    
    # Step 2. retrieve info link based on info_type parameter
    if info_type == "pokemon_team":
        member_info_link = get_pokemon_team_by_username(username)
    elif info_type == "social_media":
        member_info_link = get_social_media_by_username(username)
    else:
        raise ValueError(
            "get_member_info() has not yet been modified to retrieve values for info_type {}.".format(info_type)
        )
    
    return member_info_link