from django.db import models
from django.contrib.auth.models import User

class Student(models.Model):
    user = models.OneToOneField(User)
    is_matched = models.BooleanField(default=False)

    def __unicode__(self):
        return self.user.username

class Faculty(models.Model):
    user = models.OneToOneField(User)

    def __unicode__(self):
        return self.user.username

class Class(models.Model):
    name = models.CharField(max_length=200)

    def __unicode__(self):
        return self.name

class Group(models.Model):
    name = models.CharField(max_length=200)

    def __unicode__(self):
        return self.name

class Membership(models.Model):
    student = models.ForeignKey(Student)
    group = models.ForeignKey(Group)
