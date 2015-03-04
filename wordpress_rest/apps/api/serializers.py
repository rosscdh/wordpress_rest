# -*- coding: utf-8 -*-
from django.template.defaultfilters import slugify

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
    name = serializers.SerializerMethodField()
    value = serializers.SerializerMethodField()

    class Meta:
        model = wp_models.PostMeta
        fields = ('name', 'value')

    def get_name(self, obj):
        return obj.meta_key

    def get_value(self, obj):
        return 'test'


class PostsSerializer(serializers.ModelSerializer):
    meta = serializers.SerializerMethodField()

    class Meta:
        model = wp_models.Posts

    def get_meta(self, obj):
        return PostMetaSerializer(obj.postmeta_set.all(), many=True).data


class TermRelationshipsSerializer(serializers.ModelSerializer):
    class Meta:
        model = wp_models.TermRelationships


class TermTaxonomySerializer(serializers.ModelSerializer):
    class Meta:
        model = wp_models.TermTaxonomy


class TermsSerializer(serializers.ModelSerializer):
    parent = serializers.IntegerField(default=0)
    slug = serializers.SlugField()

    class Meta:
        model = wp_models.Terms
        fields = ('pk', 'name', 'slug', 'parent')


class CategoriesSerializer(TermsSerializer):
    taxonomy = serializers.SerializerMethodField()

    class Meta(TermsSerializer.Meta):
        fields = ('pk', 'name', 'slug', 'parent', 'taxonomy')

    def get_taxonomy(self, obj):
        return 'category'

    def create(self, validated_data):
        parent = self.data.get('parent', 0)
        taxonomy = self.data.get('taxonomy', 'category')
        import pdb;pdb.set_trace()
        validated_data['slug'] = slugify(validated_data.get('name'))

        term = self.Meta.model.objects.create(**validated_data)

        try:
            parent = wp_models.TermTaxonomy.objects.get(term=term, taxonomy=taxonomy)
        except wp_models.TermTaxonomy.DoesNotExist:
            parent = wp_models.TermTaxonomy.objects.create(term=term, taxonomy=taxonomy)
        except Exception as e:
            import pdb;pdb.set_trace()

        return term


class TagsSerializer(CategoriesSerializer):
    class Meta(CategoriesSerializer.Meta): pass

    def get_taxonomy(self, obj):
        return 'tag'


class UserMetaSerializer(serializers.ModelSerializer):
    class Meta:
        model = wp_models.UserMeta


class UsersSerializer(serializers.ModelSerializer):
    class Meta:
        model = wp_models.Users
