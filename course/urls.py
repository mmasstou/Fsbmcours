from django.urls import path, include
from course import views

app_name = "course"

urlpatterns = [
    path('<slug:moduleSlug>/', views.moduleDetails, name="module-details"),


]
