from django.shortcuts import render, redirect
from course.models import (
    Departement,
    Semester,
    Module,
    Course
)
from account.models import User
from dashboard.forms import (
    Aadd_Module_Form,
    Aadd_Course_Form
    )
from django.contrib import messages

template_name = "dashboard/"
# Create your views here.departement_view.html
def DashboardPageViews(request):
    if not request.user.is_authenticated:
        return redirect('account:login')
    Departement_qs = Departement.objects.all()
    context = {
        'Departements_sidbar':Departement_qs,
        'Departements':Departement_qs,
    }
    return render(request, "dashboard/home-ViewsPage.html", context)
def DashboardDepartement_view(request, departement):
    if not request.user.is_authenticated:
        return redirect('account:login')
    Departement_qs = Departement.objects.get(name= departement)
    Semester_qs = Semester.objects.filter(departement= Departement_qs)
    context = {
        'Departements_sidbar':Departement.objects.all(),
        'Departements':Departement_qs,
        'Semesters':Semester_qs,
    }
    return render(request, "dashboard/departement_view.html", context)
# ! Semester List View
def DashboardSemester_view(request, departement, semesterId):
    if not request.user.is_authenticated:
        return redirect('account:login')
    Departement_qs = Departement.objects.get(name= departement)
    Semester_qs = Semester.objects.get(
        departement = Departement_qs,
        slug= semesterId
        )
    Module_qs = Module.objects.filter(semester = Semester_qs)
    context = {
        'Departements_sidbar':Departement.objects.all(),
         'Departements':Departement_qs,
        'Semesters':Semester_qs,
        'Modules': Module_qs.order_by("-count", "-views")
    }
    return render(request, "dashboard/semester_view.html", context)

def Add_Module(request, departementId, semesterId):

    departement_qs = Departement.objects.get(
        name = departementId
    )
    semester_qs = Semester.objects.get(
        departement = departement_qs,
        slug = semesterId
    )
    module_qs = Module.objects.filter(
        semester = semester_qs

    )
    form = Aadd_Module_Form()
    if request.method == "POST":
        form = Aadd_Module_Form(request.POST)
        if form.is_valid():
            module_Q = form.save(commit=False)
            module_Q.semester = semester_qs
            module_Q.save()
            semester_qs.count = module_qs.count()
            semester_qs.save()
            path = request.META.get('HTTP_REFERER')
            path01 = path.split("/")[1]
            P = path[path.find("/")+2:]
            P = P[P.find("/"):].split("/Add/")[0]
            print("Path : ", P)
            return redirect(f'{P}')
        else:
            print("Error :form Is not valid")
    else:
        print("Error : method Is not POST")

    context = {
        'AddFormTitle':"Add Module To " + semester_qs.name ,
        'Departements_sidbar':Departement.objects.all(),
        'form':form
    }
    return render(request, "dashboard/add_form.html", context)

def Delete_Module(request, departementId, semesterId, moduleId):

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

    path = request.META.get('HTTP_REFERER')
    path01 = path.split("/")[1]
    P = path[path.find("/")+2:]
    P = P[P.find("/"):].split("/Add/")[0]
    print("Path : ", P)
    if request.method == "POST":
        messages.success(request, f"You have successfully Deleted {module_qs.name}")
        module_qs.delete()
        semester_qs.count -= 1
        semester_qs.save()
        return redirect(
            'dashboard:dashboard-semester-views',
            departementId,
            semesterId,
            )
    context = {
        'removeName':module_qs,
        'backURL':P,
        'Departements_sidbar':Departement.objects.all(),
    }
    return render(request, "dashboard/confirmation.html", context)


# ! module Views




def StudentsListViews(request):
    if not request.user.is_authenticated:
        return redirect('account:login')
    user_qs = User.objects.all()
    context = {
        'Departements_sidbar':Departement.objects.all(),
        "Users":user_qs,
    }
    return render(request, "dashboard/students.html", context)