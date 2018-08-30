# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# six dex numbers linked from the Member class
class PokemonTeam(models.Model):
    pokemon_team_id = models.AutoField(primary_key=True)
    pokemon_1_dex_id = models.PositiveSmallIntegerField()
    pokemon_2_dex_id = models.PositiveSmallIntegerField()
    pokemon_3_dex_id = models.PositiveSmallIntegerField()
    pokemon_4_dex_id = models.PositiveSmallIntegerField()
    pokemon_5_dex_id = models.PositiveSmallIntegerField()
    pokemon_6_dex_id = models.PositiveSmallIntegerField()

# url links to a Members social media pages
class SocialMedia(models.Model):
    social_media_id = models.AutoField(primary_key=True)
    youtube_url = models.TextField()
    twitter_url = models.TextField()
    twitch_url = models.TextField()
    soundcloud_url = models.TextField()
    favorite_switch_clip = models.TextField()

# members of the SuperFam
class Member(models.Model):
    member_id = models.AutoField(
        primary_key=True
    )
    member_lastname = models.CharField(
        max_length=32,
        blank=False,
        null=False
    )
    member_firstname = models.CharField(
        max_length=32,
        blank=False,
        null=False
    )
    member_username = models.CharField(
        max_length=32,
        unique=True,
        blank=False,
        null=False
    )
    member_age = models.PositiveSmallIntegerField()
    member_birthday = models.DateTimeField(
        blank=True,
        null=True
    )
    member_role = models.CharField(
        max_length=100,
        unique=True,
        blank=False,
        null=False
    )
    favorite_nintendo_series = models.TextField(
        blank=True,
        null=True
    )
    favorite_non_nintendo_series = models.TextField(
        blank=True,
        null=True
    )
    pokemon_team = models.ForeignKey(
        PokemonTeam,
        db_column='pokemon_team_id',
        blank=True,
        null=True,
        db_index=True,
        on_delete=models.PROTECT
    )
    social_media = models.ForeignKey(
        SocialMedia,
        db_column='social_media_id',
        blank=True,
        null=True,
        db_index=True,
        on_delete=models.PROTECT
    )