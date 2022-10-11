from django.shortcuts import render

from course.models import Course, Module

# Create your views here.

def moduleDetails(request, moduleSlug):
    Module_qs = Module.objects.get(slug=moduleSlug)
    courses_ds = Course.objects.filter(
        module = Module_qs
    )
    context = {
        "Modules":Module_qs,
        "Courses":courses_ds
    }
    return render(request, "moduleDetails.html", context)