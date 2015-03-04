# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.db import models


class CommentsMeta(models.Model):
    id = models.AutoField(db_column='meta_id', primary_key=True)
    comment = models.ForeignKey('wordpress.Comments')
    meta_key = models.CharField(max_length=255, blank=True)
    meta_value = models.TextField(blank=True)

    class Meta:
        managed = False
        db_table = 'wp_commentmeta'


class Comments(models.Model):
    id = models.AutoField(db_column='comment_ID', primary_key=True)  # Field name made lowercase.
    comment_post = models.ForeignKey('wordpress.Posts', db_column='comment_post_ID')  # Field name made lowercase.
    comment_author = models.TextField()
    comment_author_email = models.CharField(max_length=100)
    comment_author_url = models.CharField(max_length=200)
    comment_author_ip = models.CharField(db_column='comment_author_IP', max_length=100)  # Field name made lowercase.
    comment_date = models.DateTimeField()
    comment_date_gmt = models.DateTimeField()
    comment_content = models.TextField()
    comment_karma = models.IntegerField()
    comment_approved = models.CharField(max_length=20)
    comment_agent = models.CharField(max_length=255)
    comment_type = models.CharField(max_length=20)
    comment_parent = models.BigIntegerField()
    user = models.ForeignKey('wordpress.Users')

    class Meta:
        managed = False
        db_table = 'wp_comments'


class Links(models.Model):
    id = models.AutoField(db_column='link_id', primary_key=True)
    link_url = models.CharField(max_length=255)
    link_name = models.CharField(max_length=255)
    link_image = models.CharField(max_length=255)
    link_target = models.CharField(max_length=25)
    link_description = models.CharField(max_length=255)
    link_visible = models.CharField(max_length=20)
    link_owner = models.ForeignKey('wordpress.Users')
    link_rating = models.IntegerField()
    link_updated = models.DateTimeField()
    link_rel = models.CharField(max_length=255)
    link_notes = models.TextField()
    link_rss = models.CharField(max_length=255)

    class Meta:
        managed = False
        db_table = 'wp_links'


class Options(models.Model):
    id = models.AutoField(db_column='option_id', primary_key=True)
    option_name = models.CharField(unique=True, max_length=64)
    option_value = models.TextField()
    autoload = models.CharField(max_length=20)

    class Meta:
        managed = False
        db_table = 'wp_options'


class PostMeta(models.Model):
    id = models.AutoField(db_column='meta_id', primary_key=True)
    post = models.ForeignKey('wordpress.Posts')
    meta_key = models.CharField(max_length=255, blank=True)
    meta_value = models.TextField(blank=True)

    class Meta:
        managed = False
        db_table = 'wp_postmeta'


#
# Manager
#
class PostsManager(models.Manager):
    def private(self, **kwargs):
        return self.get_queryset(**kwargs).filter(post_status__in=['private'])

    def published(self, **kwargs):
        return self.get_queryset(**kwargs).filter(post_status__in=['publish'])

    def draft(self, **kwargs):
        return self.get_queryset().filter(post_status__in=['draft'])

    def auto_draft(self, **kwargs):
        return self.get_queryset(**kwargs).filter(post_status__in=['auto-draft'])

    def trash(self, **kwargs):
        return self.get_queryset(**kwargs).filter(post_status__in=['trash'])

    def inherit(self, **kwargs):
        return self.get_queryset(**kwargs).filter(post_status__in=['inherit'])


class Posts(models.Model):
    id = models.AutoField(db_column='ID', primary_key=True)  # Field name made lowercase.
    post_author = models.ForeignKey('wordpress.Users', db_column='post_author')
    post_date = models.DateTimeField()
    post_date_gmt = models.DateTimeField()
    post_content = models.TextField()
    post_title = models.TextField()
    post_excerpt = models.TextField()
    post_status = models.CharField(max_length=20)
    comment_status = models.CharField(max_length=20)
    ping_status = models.CharField(max_length=20)
    post_password = models.CharField(max_length=20)
    post_name = models.CharField(max_length=200)
    to_ping = models.TextField()
    pinged = models.TextField()
    post_modified = models.DateTimeField()
    post_modified_gmt = models.DateTimeField()
    post_content_filtered = models.TextField()
    post_parent = models.BigIntegerField()
    guid = models.CharField(max_length=255)
    menu_order = models.IntegerField()
    post_type = models.CharField(max_length=20)
    post_mime_type = models.CharField(max_length=100)
    comment_count = models.BigIntegerField()

    objects = PostsManager()

    class Meta:
        managed = False
        db_table = 'wp_posts'


class TermRelationships(models.Model):
    id = models.AutoField(primary_key=True, db_column='object_id')
    term_taxonomy = models.ForeignKey('wordpress.TermTaxonomy')
    term_order = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'wp_term_relationships'


class TermTaxonomy(models.Model):
    id = models.AutoField(primary_key=True, db_column='term_taxonomy_id')
    term = models.ForeignKey('wordpress.Terms')
    taxonomy = models.CharField(max_length=32)
    description = models.TextField(blank=True)
    parent = models.IntegerField(default=0, db_column='parent')
    count = models.BigIntegerField(default=0)

    class Meta:
        managed = False
        db_table = 'wp_term_taxonomy'


#
# Manager
#
class TermsManager(models.Manager):
    def categories(self, **kwargs):
        term_ids = [taxonomy.get('term') for taxonomy in TermTaxonomy.objects.filter(taxonomy='category').values('term')]
        return self.get_queryset().filter(pk__in=term_ids)

    def tags(self, **kwargs):
        term_ids = [taxonomy.get('term') for taxonomy in TermTaxonomy.objects.filter(taxonomy='tag').values('term')]
        return self.get_queryset().filter(pk__in=term_ids)


class Terms(models.Model):
    id = models.AutoField(db_column='term_id', primary_key=True)
    name = models.CharField(max_length=200)
    slug = models.CharField(max_length=200)
    term_group = models.BigIntegerField(default=0)

    objects = TermsManager()

    class Meta:
        managed = False
        db_table = 'wp_terms'

    def __unicode__(self):
        return u'%s' % self.name

    @property
    def parent(self):
        relation = self.termtaxonomy_set.first()
        return relation.parent if relation is not None else None


class UserMeta(models.Model):
    id = models.AutoField(db_column='umeta_id', primary_key=True)
    user = models.ForeignKey('wordpress.Users')
    meta_key = models.CharField(max_length=255, blank=True)
    meta_value = models.TextField(blank=True)

    class Meta:
        managed = False
        db_table = 'wp_usermeta'


class Users(models.Model):
    id = models.AutoField(db_column='ID', primary_key=True)  # Field name made lowercase.
    user_login = models.CharField(max_length=60)
    user_pass = models.CharField(max_length=64)
    user_nicename = models.CharField(max_length=50)
    user_email = models.CharField(max_length=100)
    user_url = models.CharField(max_length=100)
    user_registered = models.DateTimeField()
    user_activation_key = models.CharField(max_length=60)
    user_status = models.IntegerField()
    display_name = models.CharField(max_length=250)

    class Meta:
        managed = False
        db_table = 'wp_users'
