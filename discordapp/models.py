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

    class Meta:
        db_table = 'pokemon_teams'

# url links to a Members social media pages
class SocialMedia(models.Model):
    social_media_id = models.AutoField(primary_key=True)
    youtube_url = models.TextField(
        blank=True,
        null=True
    )
    twitter_url = models.TextField(
        blank=True,
        null=True
    )
    twitch_url = models.TextField(
        blank=True,
        null=True
    )
    soundcloud_url = models.TextField(
        blank=True,
        null=True
    )
    favorite_switch_clip = models.TextField(
        blank=True,
        null=True
    )

    class Meta:
        db_table = 'social_media'

# members of the SuperFam
class Member(models.Model):
    member_id = models.AutoField(
        primary_key=True
    )
    lastname = models.CharField(
        max_length=32,
        blank=False,
        null=False
    )
    firstname = models.CharField(
        max_length=32,
        blank=False,
        null=False
    )
    username = models.CharField(
        max_length=32,
        unique=True,
        blank=False,
        null=False
    )
    birthday = models.DateField(
        blank=True,
        null=True
    )
    role = models.CharField(
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
    
    class Meta:
        db_table = 'members'
        unique_together = (('firstname', 'lastname'),)