# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey has `on_delete` set to the desired behavior.
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from __future__ import unicode_literals

from django.db import models
from django.contrib.auth.models import  User
from django.urls import reverse


class TeleOld20170407(models.Model):
    ag_port = models.TextField(db_column='AG_port')  # Field name made lowercase.
    number = models.TextField(primary_key=True)
    depart = models.TextField(blank=True, null=True)
    floor = models.TextField(blank=True, null=True)
    number_110_frame = models.TextField(db_column='110_frame', blank=True, null=True)  # Field renamed because it wasn't a valid Python identifier.
    notes = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = '_tele_old_20170407'


class DjangoMigrations(models.Model):
    id = models.IntegerField(primary_key=True)  # AutoField?
    app = models.CharField(max_length=255)
    name = models.CharField(max_length=255)
    applied = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_migrations'


class Tele(models.Model):
    ag_port = models.TextField(db_column='AG_port')  # Field name made lowercase.
    number = models.TextField(primary_key=True)
    depart = models.TextField(blank=True, null=True)
    person = models.TextField(blank=True, null=True)
    floor = models.TextField(blank=True, null=True)
    number_110_frame = models.TextField(db_column='110_frame', blank=True, null=True)  # Field renamed because it wasn't a valid Python identifier.
    notes = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'tele'


class Category(models.Model):
    name = models.CharField(max_length=100)
class Tag(models.Model):
    name = models.CharField(max_length= 100)

class Post(models.Model):
    title = models.CharField(max_length= 70)
    body = models.TextField()
    created_time = models.DateTimeField()
    modified_time = models.DateTimeField()
    excerpt = models.CharField(max_length= 200, blank= True)
    category = models.ForeignKey(Category)
    tag = models.ManyToManyField(Tag, blank=True)
    author = models.ForeignKey(User)
    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return  reverse('blog:detail', kwargs={'pk': self.pk})