# -*- coding: UTF-8 -*-
from django.conf.urls import patterns  # , url

from rest_framework import routers

import views as api_views

router = routers.SimpleRouter(trailing_slash=False)

"""
Generic ViewSets
"""
router.register(r'posts', api_views.AllPostsViewset, base_name='posts')
router.register(r'published', api_views.PublishedPostsViewset, base_name='posts_published')
router.register(r'private', api_views.PrivatePostsViewset, base_name='posts_private')
router.register(r'draft', api_views.DraftPostsViewset, base_name='posts_draft')
router.register(r'trash', api_views.TrashPostsViewset, base_name='posts_trash')
router.register(r'auto_draft', api_views.AutoDraftPostsViewset, base_name='posts_auto_draft')

router.register(r'links', api_views.LinksViewset, base_name='links')
router.register(r'comments', api_views.CommentsViewset, base_name='comments')

router.register(r'options', api_views.OptionsViewset, base_name='options')

router.register(r'taxonomy', api_views.TermTaxonomyViewset, base_name='taxonomy')
router.register(r'terms', api_views.TermsViewset, base_name='terms')
router.register(r'categories', api_views.CategoriesViewset, base_name='categories')
router.register(r'tags', api_views.TagsViewset, base_name='tags')

router.register(r'users', api_views.UsersViewset, base_name='users')


urlpatterns = patterns('',
  # Custom Compound viewsets
) + router.urls
