from django.urls import path, include 
from dashboard import views 
from dashboard import course
app_name = "dashboard" 

urlpatterns = [
    path('Students/', views.StudentsListViews, name="students-list-views"),
    path('', views.DashboardPageViews, name="indexpage_view"),
    path('<slug:departement>/', views.DashboardDepartement_view, name="dashboard_departement_views"),
    path('<slug:departement>/<slug:semesterId>/', views.DashboardSemester_view, name="dashboard-semester-views"),
    path('<slug:departementId>/<slug:semesterId>/Add/', views.Add_Module, name="dashboard-add-module"),
    path('<slug:departementId>/<slug:semesterId>/<slug:moduleId>/', course.DashboardModuleView, name="dashboard-module-views"),
    path('<slug:departementId>/<slug:semesterId>/<slug:moduleId>/Add/', course.Add_Course, name="dashboard-add-course"),
    path('<slug:departementId>/<slug:semesterId>/<slug:moduleId>/delete/', views.Delete_Module, name="dashboard-delete-module"),
    path('<slug:departementId>/<slug:semesterId>/<slug:moduleId>/<courseName>/delete/', course.Delete_Course, name="dashboard-delete-course"),
    path('<slug:departementId>/<slug:semesterId>/<slug:moduleId>/<courseName>/Edit/', course.Edit_Course, name="dashboard-edit-course"),

]
