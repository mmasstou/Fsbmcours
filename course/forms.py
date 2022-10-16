from django.forms import ModelForm
from django.contrib.auth.forms import UserCreationForm
from course.models import *


class Adding_courseForm(ModelForm):
    class Meta:
        model = Course
        fields = ['name', 'course_file']
