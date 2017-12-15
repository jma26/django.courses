# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.db import models

# Create your models here.
class CourseManager(models.Manager):
    def basic_validator(self, postData):
        errors = []
        if len(postData['name']) < 5:
            errors.append("Name field must be at least 5 characters or more")
        if len(postData['description']) < 15:
            errors.append("Description field must be at least 10 characters or more")
        return errors

class Course(models.Model):
    name = models.CharField(max_length = 255)
    desc = models.TextField()
    created_at = models.DateTimeField(auto_now_add = True)

    objects = CourseManager()
