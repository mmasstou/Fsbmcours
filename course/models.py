from __future__ import unicode_literals
from tkinter.tix import Tree
from django.db import models
from django.utils.text import slugify
from django.urls import reverse
import os
import uuid
import random
from account.models import User
import datetime

class setteings(models.Model):
    Darktheme = models.BooleanField(default=False)
    def __str__(self):
        return self.Darktheme
        
def getFileName(request, filename):
	
	# origiFilename = filename
	timeNow = datetime.datetime.now().strftime('%Y%m%d%H:%M:%S')
	timeNow_dir = datetime.datetime.now().strftime('%Y%m_%d')
	# filename = "%s%s" % (timeNow, origiFilename)
	upload_to = 'Course_Pdfs/'+ timeNow_dir + '/'
	return os.path.join(upload_to, filename)

"""
---> module.py
        +   departement " -physique  ... "
        +   semester  "semester 1 ..."
        +   modeles "mecanique de point ... "
        +   couses " td ... "
"""
class Departement(models.Model):
    name = models.TextField(max_length=15)
    veiw = models.IntegerField(default=0)
    count = models.IntegerField(default=0)

    class Meta:
        ordering = ['-name']

    def __str__(self):
        return self.name
    def getdashboard_departement_viewssURL(self):
        return reverse("dashboard:dashboard_departement_views", kwargs={"departement":self.name})
class Semester(models.Model):
    name = models.CharField(max_length=200)
    auther = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    departement = models.ForeignKey(Departement, on_delete=models.SET_NULL, null=True)
    semester_participants = models.ManyToManyField(User, related_name='semester_participants', blank=True)
    numberOfParticipent =  models.IntegerField(default=0)
    veiw = models.IntegerField(default=0)
    count = models.IntegerField(default=0)
    slug = models.SlugField(null=True, blank= True)

    def save(self, *args, **kwargs):

        if self.slug == None:
            slug = slugify(self.name)
            self.slug = slug
        super().save(*args, **kwargs)

    class Meta:
        ordering = ['-name']
    def getSemesterViewsURL(self):
        return reverse("course:semester-views",
        kwargs={
            "departementId": self.departement.name,
            "semesterId": self.slug
            })
    def getDashboardSemesterViewsURL(self):
        d_qs = Departement.objects.get(
            name = self.departement.name
        )
        return reverse("dashboard:dashboard-semester-views",
        kwargs={
            "departement":d_qs,
            "semesterId": self.slug
            })
    def AddModuleURL(self):
        return reverse("dashboard:dashboard-add-module",
        kwargs={
            "departementId": self.departement.name,
            "semesterId":self.slug
            })
    def __str__(self):
        return self.name

class Module(models.Model):
    name = models.CharField(max_length=200)
    veiw = models.IntegerField(default=0)
    count = models.IntegerField(default=0)
    semester = models.ForeignKey(Semester, on_delete=models.SET_NULL, null=True)
    ispublic = models.BooleanField(default=False, null=True, blank=True)
    updated = models.DateTimeField(auto_now=True)
    created = models.DateTimeField(auto_now_add=True)
    slug = models.SlugField(null=True, blank= True)

    def save(self, *args, **kwargs):

        if self.slug == None:
            slug = slugify(self.name)
            self.slug = slug
        super().save(*args, **kwargs)


    class Meta:
        ordering = ['-updated','-created',]

    def getModuleViewsURL(self):
        return reverse("course:module-details",
        kwargs={
            "departementId":self.semester.departement.name,
            "semesterId": self.semester.slug,
            "moduleSlug":self.slug
            })
    def getDashboardModuleViewsURL(self):
        return reverse("dashboard:dashboard-module-views",
        kwargs={
            "departementId":self.semester.departement.name,
            "semesterId": self.semester.slug,
            "moduleId":self.slug
            })
    def AddCourseURL(self):
        return reverse("dashboard:dashboard-add-course",
        kwargs={
            "departementId": self.semester.departement.name,
            "semesterId":self.semester.slug,
            "moduleId": self.slug
            })
    def __str__(self):
        return self.name

class Course(models.Model):
    name = models.CharField(max_length=200)
    module = models.ForeignKey(Module, on_delete=models.SET_NULL, null=True)
    course_file = models.FileField(upload_to=getFileName) 
    veiw = models.IntegerField(default=0)
    count = models.IntegerField(default=0)
    updated = models.DateTimeField(auto_now=True)
    created = models.DateTimeField(auto_now_add=True)
    @property
    def pdfURL(self):
        try:
            url = self.course_file.url
        except:
            url = ''
        return url
    class Meta:
        ordering = ['-created']

    def DeleteCourseURL(self):
        return reverse("dashboard:dashboard-delete-course",
        kwargs={
            "departementId": self.module.semester.departement.name,
            "semesterId":self.module.semester.slug,
            "moduleId": self.module.slug,
            "courseName":self.name
        })
    def EditCourseURL(self):
        return reverse("dashboard:dashboard-edit-course",
        kwargs={
            "departementId": self.module.semester.departement.name,
            "semesterId":self.module.semester.slug,
            "moduleId": self.module.slug,
            "courseName":self.name
        })
    def __str__(self):
        return self.name[:50]


# 