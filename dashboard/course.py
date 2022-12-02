from django.shortcuts import render, redirect
from django.contrib import messages
from course.models import (
    Departement,
    Semester,
    Module,
    Course
)
from dashboard.forms import (
    Aadd_Course_Form
    )

def DashboardModuleView(request, departementId, semesterId, moduleId):
    departement_qs = Departement.objects.get(
        name = departementId
    )
    semester_qs = Semester.objects.get(
        departement = departement_qs,
        slug = semesterId
    )
    module_qs = Module.objects.get(
        semester = semester_qs,
        slug = moduleId
    )
    course_qs = Course.objects.filter(
        module = module_qs
    )
    context = {
        'Departements_sidbar':Departement.objects.all(),
        "Departements":departement_qs,
        "Semesters":semester_qs,
        "Modules":module_qs,
        "Courses":course_qs
    }
    return render(request, "dashboard/module_view.html", context)


def Add_Course(request, departementId, semesterId, moduleId):

    departement_qs = Departement.objects.get(
        name = departementId
    )
    semester_qs = Semester.objects.get(
        departement = departement_qs,
        slug = semesterId
    )
    module_qs = Module.objects.get(
        semester = semester_qs,
        slug = moduleId
    )
    course_qs = Course.objects.filter(
        module = module_qs
    )
    path = request.META.get('HTTP_REFERER')
    path01 = path.split("/")[1]
    P = path[path.find("/")+2:]
    P = P[P.find("/"):].split("/Add/")[0]
    print("Path : ", P)
    form = Aadd_Course_Form()
    if request.method == "POST":
        form = Aadd_Course_Form(request.POST, request.FILES)
        if form.is_valid():
            Course_Q = form.save(commit=False)
            Course_Q.module = module_qs
            if course_qs.filter(name = Course_Q.name).count() > 0 :
                messages.error(request, f"Duplicate {Course_Q.name}")
                return redirect(f'{P}')
            Course_Q.save()
            module_qs.count = course_qs.count()
            module_qs.save()
           
            return redirect(f'{P}')
        else:
            print("Error :form Is not valid")
    else:
        print("Error : method Is not POST")

    context = {
        'AddFormTitle':"Add Course To " + module_qs.name ,
        'Departements_sidbar':Departement.objects.all(),
        'form':form
    }
    return render(request, "dashboard/add_form.html", context)

def Edit_Course(request, departementId, semesterId, moduleId, courseName):

    departement_qs = Departement.objects.get(
        name = departementId
    )
    semester_qs = Semester.objects.get(
        departement = departement_qs,
        slug = semesterId
    )
    module_qs = Module.objects.get(
        semester = semester_qs,
        slug = moduleId
    )
    course_qs = Course.objects.filter(
        module = module_qs
    )
    course_instance = Course.objects.get(
        name = courseName,
        module = module_qs
    )
    path = request.META.get('HTTP_REFERER')
    path01 = path.split("/")[1]
    P = path[path.find("/")+2:]
    P = P[P.find("/"):].split("/Edit/")[0]
    print("Path : ", P)
    form = Aadd_Course_Form(instance=course_instance)
    if request.method == "POST":
        form = Aadd_Course_Form(request.POST, request.FILES, instance=course_instance)
        if form.is_valid():
            Course_Q = form.save(commit=False)
            if course_qs.filter(name = Course_Q.name).count() > 0 and (Course_Q.pk != course_qs.get(name = Course_Q.name).pk):
                messages.error(request, f"Duplicate '{Course_Q.name}'")
            else :
                Course_Q.save()
                messages.success(request, f"You have successfully updated {Course_Q.name}")
            return redirect(
                'dashboard:dashboard-module-views',
                departementId,
                semesterId,
                moduleId
            )
        else:
            print("Error :form Is not valid")
    else:
        print("Error : method Is not POST")

    context = {
        'type':True,
        'AddFormTitle':"Edit " + module_qs.name ,
        'Departements_sidbar':Departement.objects.all(),
        'form':form
    }
    return render(request, "dashboard/add_form.html", context)

def Delete_Course(request, departementId, semesterId, moduleId, courseName):

    departement_qs = Departement.objects.get(
        name = departementId
    )
    semester_qs = Semester.objects.get(
        departement = departement_qs,
        slug = semesterId
    )
    module_qs = Module.objects.get(
        semester = semester_qs,
        slug = moduleId
    )
    course_qs = Course.objects.get(
        name = courseName,
        module = module_qs
    )
    path = request.META.get('HTTP_REFERER')
    path01 = path.split("/")[1]
    P = path[path.find("/")+2:]
    P = P[P.find("/"):].split("/Add/")[0]
    print("Path : ", P)
    if request.method == "POST":
        messages.success(request, f"You have successfully Deleted {course_qs.name}")
        course_qs.delete()
        module_qs.count -= 1
        module_qs.save()
        return redirect(
            'dashboard:dashboard-module-views',
            departementId,
            semesterId,
            moduleId
            )
    context = {
        'removeName':course_qs,
        'backURL':P,
        'Departements_sidbar':Departement.objects.all(),
    }
    return render(request, "dashboard/confirmation.html", context)

