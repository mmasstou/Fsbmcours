from django.urls import path, include
from account import views

app_name = "account"

urlpatterns = [
    path('login/', views.loginPage, name="login"),
    path('logout/', views.logoutUser, name="logout"),
    path('register/', views.registerPage, name="register"),
    path('activate/<uidb64>/<token>', views.activate, name='activate'),

]
