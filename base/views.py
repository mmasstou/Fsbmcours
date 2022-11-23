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

from account.models import WebConfigirations
@csrf_exempt
def indexPage(request):
    # if not request.user.is_authenticated:
    #     return redirect('account:login')
    # form = MyForm()

    # if request.method == 'POST':
    #     form = MyForm(request.POST)
    #     if form.is_valid():
    #         form.save()
    them = ""
    q = request.GET.get('q') if request.GET.get('q') != None else ''
    if request.user.is_authenticated:
        WebConfig_qs, created = WebConfigirations.objects.get_or_create(
            useradmin=request.user)
    else:
        WebConfig_qs, created = WebConfigirations.objects.get_or_create(
            name="defualt_user")
        print("New config is created >>>>>>>> ")
    module_qs = Module.objects.filter(
        Q(name__icontains = q)
        )
    course_size = module_qs.count()
    try:
        print("theme : " + request.user.theme)
        them = "dark_active" if request.user.theme == "dark" else ""
        print("q : " + q)
    except:
        product_qs = ""
    course_qs = Course.objects.all()
    # module_qs = Module.objects.all()
    Departement_qs = Departement.objects.all()
    semmester_ds = Semester.objects.all()
    context = {
        "WebConfig_qs":WebConfig_qs,
        # "them":them,
        "modules": module_qs,
        "course_size":course_size,
        "Departements": Departement_qs,
        "semmesters":semmester_ds
    }
    return render(request, 'index.html', context)

