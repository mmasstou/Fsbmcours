from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.db.models import Q
from django.contrib.auth import authenticate, login, logout
from django.template import *
from django.http import HttpRequest , HttpResponseRedirect
from django.conf import settings
from django.shortcuts import redirect
from django.views.decorators.csrf import csrf_exempt
from django.core.mail import send_mail
from django.urls import reverse
from course.models import *
from django.contrib.auth import forms

def indexPage(request):
    # if not request.user.is_authenticated:
    #     return redirect('account:login')
    # form = MyForm()

    # if request.method == 'POST':
    #     form = MyForm(request.POST)
    #     if form.is_valid():
    #         form.save()
    print("theme : " + request.user.theme)
    them = "dark_active" if request.user.theme == "dark" else ""
    q = request.GET.get('q') if request.GET.get('q') != None else ''
    try:
        print("q : " + q)
        module_qs = Module.objects.filter(
            name__icontains = q
            )
    except:
        product_qs = ""
    course_qs = Course.objects.all()
    # module_qs = Module.objects.all()
    course_size = module_qs.count()
    Departement_qs = Departement.objects.all()
    semmester_ds = Semester.objects.all()
    context = {
        "them":them,
        "modules": module_qs,
        "course_size":course_size,
        "Departements": Departement_qs,
        "semmesters":semmester_ds
    }
    return render(request, 'index.html', context)

