# -*- coding: utf-8 -*-
from rest_framework import serializers

import wordpress_rest.apps.wordpress.models as wp_models


class CommentMetaSerializer(serializers.ModelSerializer):
    class Meta:
        model = wp_models.CommentsMeta


class CommentsSerializer(serializers.ModelSerializer):
    class Meta:
        model = wp_models.Comments


class LinksSerializer(serializers.ModelSerializer):
    class Meta:
        model = wp_models.Links


class OptionsSerializer(serializers.ModelSerializer):
    class Meta:
        model = wp_models.Options


class PostMetaSerializer(serializers.ModelSerializer):
    class Meta:
        model = wp_models.PostMeta


class PostsSerializer(serializers.ModelSerializer):
    class Meta:
        model = wp_models.Posts


class TermRelationshipsSerializer(serializers.ModelSerializer):
    class Meta:
        model = wp_models.TermRelationships


class TermTaxonomySerializer(serializers.ModelSerializer):
    class Meta:
        model = wp_models.TermTaxonomy


class TermsSerializer(serializers.ModelSerializer):
    class Meta:
        model = wp_models.Terms


class UserMetaSerializer(serializers.ModelSerializer):
    class Meta:
        model = wp_models.UserMeta


class UsersSerializer(serializers.ModelSerializer):
    class Meta:
        model = wp_models.Users
