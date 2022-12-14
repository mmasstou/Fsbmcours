from django.shortcuts import render, redirect
from course.models import Course, Module, Semester, Departement
from .forms import Adding_courseForm
# Create your views here.

def moduleDetails(request,departementId, semesterId, moduleSlug):
    departement_qs = Departement.objects.get(name = departementId)
    semester_qs = Semester.objects.get(
        departement = departement_qs,
        slug = semesterId
    )
    Module_qs = Module.objects.get(
        semester = semester_qs,
        slug=moduleSlug
        )
    courses_ds = Course.objects.filter(
        module = Module_qs
    )
    Module_qs.views += 1
    Module_qs.save()
    context = {
        "Semesters":semester_qs,
        "course_size":courses_ds.count(),
        "title":Module_qs.name,
        "Modules":Module_qs,
        "Courses":courses_ds
    }
    return render(request, "moduleDetails.html", context)
def semesterViews(request,departementId, semesterId):
    departement_qs = Departement.objects.get(
        name = departementId
    )
    semester_qs = Semester.objects.get(
        departement = departement_qs,
        slug = semesterId
        )
    module_qs = Module.objects.filter(semester = semester_qs)
    semester_qs.views += 1
    semester_qs.save()
    context = {
        "Semesters":semester_qs,
        "Modules":module_qs
    }
    return render(request, "semster_views.html", context)
# ? admin panel

def Add_course(request, moduleSlug):
    Module_qs = Module.objects.get(slug=moduleSlug)
    courses_ds = Course.objects.filter(
        module = Module_qs
    )

    form = Adding_courseForm()
    if request.method == 'POST':
        form = Adding_courseForm(request.POST, request.FILES)
        if form.is_valid():
            cs = form.save(commit = False)
            cs.module = Module_qs
            cs.save()
            Module_qs.count = courses_ds.count()
            Module_qs.save()
            return redirect('course:module-details', moduleSlug )
    context = {
        "form":form,
        "Modules":Module_qs,
        "Courses":courses_ds
    }
    return render(request, "add.html", context)

def edit_course(request, moduleSlug, course_slug):
    Module_qs = Module.objects.get(slug=moduleSlug)
    courses_ds = Course.objects.get(
        module = Module_qs,
        slug = course_slug
    )

    form = Adding_courseForm(instance=courses_ds)
    if request.method == 'POST':
        form = Adding_courseForm(request.POST, request.FILES, instance=courses_ds)
        if form.is_valid():
            cs = form.save(commit = False)
            cs.module = Module_qs
            cs.save()
            return redirect('course:module-details', moduleSlug )
    context = {
        "form":form,
        "Modules":Module_qs,
        "Courses":courses_ds
    }
    return render(request, "add.html", context)

def Delete_course(request, moduleSlug, course_slug):
    Module_qs = Module.objects.get(slug=moduleSlug)
    courses_ds = Course.objects.get(
        module = Module_qs,
        slug = course_slug
    )
    courses_ds.delete()
    return redirect('course:module-details', moduleSlug )