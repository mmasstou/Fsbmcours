from django.forms import ModelForm
from django.contrib.auth.forms import UserCreationForm
from course.models import (
    Module,
    Course
    )


class Aadd_Module_Form(ModelForm):
    class Meta:
        model = Module
        fields = ['name']



class Aadd_Course_Form(ModelForm):
    class Meta:
        model = Course
        fields = ['name', 'course_file']
