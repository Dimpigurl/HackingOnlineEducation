# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.contrib.auth.models import User
from django.db import models

# Create your models here.
#sign up form for newsletter not login or contact
class SignUp(models.Model):
     full_name=models.CharField(max_length=60,blank=True)
     email=models.EmailField()

     def __unicode__(self):
         return self.email


class UserProfile(models.Model):
    user = models.OneToOneField(User)
    phone=models.CharField(max_length=10)
    designation=models.CharField(max_length=20)
    image=models.ImageField(upload_to='profile_images', blank=False)

    def __unicode__(self):
        return self.user.username

class Categories(models.Model):
    category_name=models.CharField(max_length=30,null=False)
    url=models.URLField()
    description=models.TextField()
    rating=models.IntegerField()
    image=models.ImageField(upload_to='categories', blank=True)
    sort=models.CharField(max_length=30,default='courses')
    def __unicode__(self):
        return self.category_name

class Pages(models.Model):
    category=models.ForeignKey(Categories,on_delete=models.CASCADE,null=True)
    name=models.CharField(max_length=30,null=False)
    rating=models.IntegerField()
    url=models.URLField()
    def __unicode__(self):
        return self.name

class Course(models.Model):
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    course=models.CharField(max_length=50)
    timestamp=models.TimeField()
    def __unicode__(self):
        return self.course

class StandAlone(models.Model):
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    name=models.CharField(max_length=50)
    url=models.URLField()
    description=models.TextField()
    image=models.ImageField(upload_to='course')
    def __unicode__(self):
        return self.name

class Challenge(models.Model):
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    name=models.CharField(max_length=50)
    url=models.URLField()
    description=models.TextField()
    rating=models.IntegerField()
    image=models.ImageField(upload_to='course')
    def __unicode__(self):
        return self.name

class Code100(models.Model):
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    timestamp=models.TimeField()
    started=models.BooleanField()
    done=models.BooleanField(blank=True)
    def __unicode__(self):
        return self.started
