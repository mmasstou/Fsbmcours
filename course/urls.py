from django.urls import path, include
from course import views

app_name = "course"

urlpatterns = [
    path('<slug:moduleSlug>/', views.moduleDetails, name="module-details"),
    path('<slug:moduleSlug>/add', views.Add_course, name="add-course"),
    path('<slug:moduleSlug>/<course_slug>/delete', views.Delete_course, name="delete-course"),
    path('<slug:moduleSlug>/<course_slug>/edit', views.edit_course, name="edit-course"),


]
