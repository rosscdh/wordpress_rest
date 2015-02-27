# -*- coding: utf-8 -*-
from rest_framework import serializers

import wordpress_rest.apps.wordpress.models as wp_models


class CommentMetaSerializer(serializers.ModelSerializer):
    class Meta:
        model = wp_models.CommentsMeta
        queryset = wp_models.CommentsMeta.objects.all()


class CommentsSerializer(serializers.ModelSerializer):
    class Meta:
        model = wp_models.Comments
        queryset = wp_models.Comments.objects.all()


class LinksSerializer(serializers.ModelSerializer):
    class Meta:
        model = wp_models.Links
        queryset = wp_models.Links.objects.all()


class OptionsSerializer(serializers.ModelSerializer):
    class Meta:
        model = wp_models.Options
        queryset = wp_models.Options.objects.all()


class PostMetaSerializer(serializers.ModelSerializer):
    class Meta:
        model = wp_models.PostMeta
        queryset = wp_models.PostMeta.objects.all()


class PostsSerializer(serializers.ModelSerializer):
    class Meta:
        model = wp_models.Posts
        queryset = wp_models.Posts.objects.all()


class TermRelationshipsSerializer(serializers.ModelSerializer):
    class Meta:
        model = wp_models.TermRelationships
        queryset = wp_models.TermRelationships.objects.all()


class TermTaxonomySerializer(serializers.ModelSerializer):
    class Meta:
        model = wp_models.TermTaxonomy
        queryset = wp_models.TermTaxonomy.objects.all()


class TermsSerializer(serializers.ModelSerializer):
    class Meta:
        model = wp_models.Terms
        queryset = wp_models.Terms.objects.all()


class UserMetaSerializer(serializers.ModelSerializer):
    class Meta:
        model = wp_models.UserMeta
        queryset = wp_models.UserMeta.objects.all()


class UsersSerializer(serializers.ModelSerializer):
    class Meta:
        model = wp_models.Users
        queryset = wp_models.Users.objects.all()
