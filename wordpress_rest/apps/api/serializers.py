# -*- coding: utf-8 -*-
from django.template.defaultfilters import slugify
from django.utils.encoding import smart_text

from rest_framework import serializers

import wordpress_rest.apps.wordpress.models as wp_models
import phpserialize
import json
import ast


def _decode_php_serialized_value(value):
    """
    Nasty method to decode data that should REALLY be json not goddamned php serialize
    """
    for i in range(0,5):
        try:
            value = phpserialize.loads(value)
        except ValueError as e:
            break
        except:
            value = 'Unable to deserialize from php'
    try:
        value = ast.literal_eval(value)
    except:
        # probably a string
        pass

    if type(value) in [dict]:
        # handle unicode values
        value = json.dumps(value)  # convert to json string
        value = json.loads(smart_text(value))  # convert back
    else:
        value = smart_text(value)

    return value


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
        return smart_text(obj.meta_key)

    def get_value(self, obj):
        return _decode_php_serialized_value(obj.value)


class PostsSerializer(serializers.ModelSerializer):
    meta = serializers.SerializerMethodField()
    images = serializers.SerializerMethodField()

    class Meta:
        model = wp_models.Posts
        queryset = wp_models.Posts.objects.select_related('meta').all()

    def get_meta(self, obj):
        meta = dict()
        for m in obj.postmeta_set.all().iterator():
            m = PostMetaSerializer(m).data

            name = m.get('name')
            value = m.get('value')

            if name in meta:
                if type(meta[name]) is not list:
                    tmp_value = meta[name]
                    meta[name] = [tmp_value]
                else:
                    meta[name].append(value)

            else:
                meta[name] = value
        return meta

    def get_images(self, obj):
        return obj.images()



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

        validated_data['slug'] = slugify(validated_data.get('name'))

        term = self.Meta.model.objects.create(**validated_data)

        try:
            parent = wp_models.TermTaxonomy.objects.get(term=term, taxonomy=taxonomy)

        except wp_models.TermTaxonomy.DoesNotExist:
            parent = wp_models.TermTaxonomy.objects.create(term=term, taxonomy=taxonomy)

        except Exception as e:
            pass

        return term


class TagsSerializer(CategoriesSerializer):

    def get_taxonomy(self, obj):
        return 'tag'


class UserMetaSerializer(serializers.ModelSerializer):
    class Meta:
        model = wp_models.UserMeta


class UsersSerializer(serializers.ModelSerializer):
    class Meta:
        model = wp_models.Users
