from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.db.models import Q
from django.contrib.auth import authenticate, login, logout
from .models import User
from .forms import UserForm, MyUserCreationForm
from django.template import *
from django.http import HttpRequest , HttpResponseRedirect
from django.conf import settings
from django.shortcuts import redirect
from django.views.decorators.csrf import csrf_exempt
from django.core.mail import send_mail
from django.urls import reverse
# Create your views here.

def loginPage(request):
    page = 'login'
    if request.user.is_authenticated:
        return redirect('index')

    if request.method == 'POST':
        username = request.POST.get('username').lower()
        password = request.POST.get('password')
        print(" username :", username)
        print(" password :", password)
        try:
            user = User.objects.get(username=username)
        except:
            messages.error(request, 'User does not exist')
        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            p = request.META.get('HTTP_REFERER')
            print("                                     >>>>" + p)
            try:
                path01 = p.split("?next=")[1]
            except :
                path01 = ""
            path02 = p.split("/login")[0]
            print(path01)
            print(path02)
            # return redirect(f'{path}')
            # return HttpResponseRedirect(next)
            p = path02 + path01
            return redirect(f'{p}')
        else:
            messages.error(request, 'Username OR password does not exit')

    context = {'page': page}
    template__name = "login.html"
    return render(request, template__name, context)

def logoutUser(request):
    logout(request)
    path = request.META.get('HTTP_REFERER')
    return redirect(f'{path}')


from django.utils.http import urlsafe_base64_decode, urlsafe_base64_encode
from django.contrib.sites.shortcuts import get_current_site
from django.template.loader import render_to_string
from django.utils.encoding import force_bytes, force_str
from .tokens import generate_token
from django.core.mail import EmailMessage, send_mail

def registerPage(request):
    if request.user.is_authenticated:
        return redirect('index')
    form = MyUserCreationForm()

    if request.method == 'POST':
        form = MyUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            fname = user.first_name.lower()
            lname = user.last_name.lower()
            user.username = fname[:1] + lname[:7] + "_fs"
            user.save()
            login(request, user)

            # # Welcome Email
            # subject = "Welcome to GFG- Django Login!!"
            # message = "Hello " + user.first_name + "!! \n" + "Welcome to GFG!! \nThank you for visiting our website\n. We have also sent you a confirmation email, please confirm your email address. \n\nThanking You\nAnubhav Madhav"        
            # from_email = settings.EMAIL_HOST_USER
            # to_list = [user.email]
            # send_mail(subject, message, from_email, to_list, fail_silently=True)
            
            # # Email Address Confirmation Email
            # current_site = get_current_site(request)
            # email_subject = "Confirm your Email @ GFG - Django Login!!"
            # token = generate_token.make_token(user)
            # message2 = render_to_string('email_confirmation.html',{
                
            #     'name': user.first_name,
            #     'domain': current_site.domain,
            #     'uid': urlsafe_base64_encode(force_bytes(user.pk)),
            #     'token': token
            # })
            # print("name :" + user.first_name)
            # print("domain :" + current_site.domain)
            # print("uid :" + urlsafe_base64_encode(force_bytes(user.username)))
            # print("token :" + token)
            # email = EmailMessage(
            # email_subject,
            # message2,
            # settings.EMAIL_HOST_USER,
            # [user.email],
            # )
            # email.fail_silently = False
            # email.send()
            # p = request.META.get('HTTP_REFERER')
            # try:
            #     path01 = p.split("?next=")[1]
            # except :
            #     path01 = ""
            # path02 = p.split("/register")[0]
            # print(path01)
            # print(path02)
            # # return redirect(f'{path}')
            # # return HttpResponseRedirect(next)
            # p = path02 + path01
            return redirect("account:login")
        else:
            messages.error(request, 'An error occurred during registration')

    return render(request, 'register.html', {'form': form})

def activate(request,uidb64,token):
    try:
        uid = force_str(urlsafe_base64_decode(uidb64))
        myuser = User.objects.get(pk=uid)
    except (TypeError,ValueError,OverflowError,User.DoesNotExist):
        myuser = None

    if myuser is not None and generate_token.check_token(myuser,token):
        myuser.is_active = True
        # user.profile.signup_confirmation = True
        myuser.save()
        login(request,myuser)
        messages.success(request, "Your Account has been activated!!")
        return redirect('acount:login')
    else:
        return render(request,'register.html')


def User_profile(request,username):
    context = {}
    return render(request, "profile.html", context)