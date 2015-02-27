# -*- coding: utf-8 -*-
#from django.shortcuts import get_object_or_404

from rest_framework.response import Response
from rest_framework import viewsets
from rest_framework import status as http_status


import wordpress_rest.apps.wordpress.models as wp_models
import serializers as api_serializers


class CommentsViewset(viewsets.ModelViewSet):
    model = wp_models.Comments
    serializer_class = api_serializers.CommentsSerializer
    queryset = wp_models.Comments.objects.all()


class LinksViewset(viewsets.ModelViewSet):
    model = wp_models.Links
    serializer_class = api_serializers.LinksSerializer
    queryset = wp_models.Links.objects.all()


class OptionsViewset(viewsets.ModelViewSet):
    model = wp_models.Options
    serializer_class = api_serializers.OptionsSerializer
    queryset = wp_models.Options.objects.all()


class PostsViewset(viewsets.ModelViewSet):
    model = wp_models.Posts
    serializer_class = api_serializers.PostsSerializer
    queryset = wp_models.Posts.objects.all()


class TermRelationshipsViewset(viewsets.ModelViewSet):
    model = wp_models.TermRelationships
    serializer_class = api_serializers.TermRelationshipsSerializer
    queryset = wp_models.TermRelationships.objects.all()


class TermTaxonomyViewset(viewsets.ModelViewSet):
    model = wp_models.TermTaxonomy
    serializer_class = api_serializers.TermTaxonomySerializer
    queryset = wp_models.TermTaxonomy.objects.all()


class TermsViewset(viewsets.ModelViewSet):
    model = wp_models.Terms
    serializer_class = api_serializers.TermsSerializer
    queryset = wp_models.Terms.objects.all()


class CategoriesViewset(viewsets.ModelViewSet):
    model = wp_models.Terms
    serializer_class = api_serializers.TermsSerializer
    queryset = wp_models.Terms.objects.categories()


class TagsViewset(viewsets.ModelViewSet):
    model = wp_models.Terms
    serializer_class = api_serializers.TermsSerializer
    queryset = wp_models.Terms.objects.tags()


class UsersViewset(viewsets.ModelViewSet):
    model = wp_models.Users
    serializer_class = api_serializers.UsersSerializer
    queryset = wp_models.Users.objects.all()
