# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models


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
    bio = models.TextField(
        blank=True,
        null=True
    )
    favorite_nintendo_series = models.TextField(
        blank=True,
        null=True
    )
    favorite_non_nintendo_series = models.TextField(
        blank=True,
        null=True
    )
    
    class Meta:
        db_table = 'all_members'
        unique_together = (('firstname', 'lastname'),)


# youtube channels under the SuperFam banner
class Project(models.Model):
    project_id = models.AutoField(
        primary_key=True
    )
    title = models.CharField(
        max_length=100,
        unique=True,
        blank=False,
        null=False
    )
    url = models.TextField(
        # TODO - unique=True,  # when actual data is inserted
        blank=False,
        null=False
    )

    class Meta:
        db_table = 'all_projects'


# roles that a Member can play in a Project
class ProjectRole(models.Model):
    project_role_id = models.AutoField(
        primary_key=True
    )
    project_role_name = models.CharField(
        max_length=100,
        unique=True,
        blank=False,
        null=False
    )
    project_role_description = models.TextField(
        blank=False,
        null=True
    )

    class Meta:
        db_table = 'all_project_roles'
        unique_together = (('project_role_name', 'project_role_description'))


# links a Member to pokemon team data
class LinkMemberPokemon(models.Model):
    link_member_pokemon_id = models.AutoField(primary_key=True)
    member_id = models.ForeignKey(
        Member,
        db_column="member_id",
        blank=False,
        null=False
    )
    pokemon_1_dex_id = models.PositiveSmallIntegerField()
    pokemon_2_dex_id = models.PositiveSmallIntegerField()
    pokemon_3_dex_id = models.PositiveSmallIntegerField()
    pokemon_4_dex_id = models.PositiveSmallIntegerField()
    pokemon_5_dex_id = models.PositiveSmallIntegerField()
    pokemon_6_dex_id = models.PositiveSmallIntegerField()

    class Meta:
        db_table = 'link_members_pokemon'


# links a Member to Projects with a ProjectRole
class LinkMemberProject(models.Model):
    link_member_project_id = models.AutoField(
        primary_key=True
    )
    member_id = models.ForeignKey(
        Member,
        db_column="member_id",
        blank=False,
        null=False
    )
    project_id = models.ForeignKey(
        Project,
        db_column="project_id",
        blank=False,
        null=False
    )
    project_role = models.ForeignKey(
        ProjectRole,
        db_column="project_role_id",
        blank=False,
        null=False
    )

    class Meta:
        db_table = 'link_members_projects'
        unique_together = (('member_id', 'project_id', 'project_role'))


# links a Member to social media data
class LinkMemberSocialMedia(models.Model):
    social_media_id = models.AutoField(primary_key=True)
    member_id = models.ForeignKey(
        Member,
        db_column="member_id",
        blank=False,
        null=False
    )
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
    favorite_switch_clip_url = models.TextField(
        blank=True,
        null=True
    )

    class Meta:
        db_table = 'link_members_social_media'