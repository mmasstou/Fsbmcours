from django.urls import path, include 
from dashboard import views 

app_name = "dashboard"

urlpatterns = [
    path('Students/', views.StudentsListViews, name="students-list-views"),
    path('', views.DashboardPageViews, name="indexpage_view"),
    path('<slug:departement>/', views.DashboardDepartement_view, name="dashboard_departement_views"),
    path('<slug:departement>/<slug:semesterId>/', views.DashboardSemester_view, name="dashboard-semester-views"),
    path('<slug:departementId>/<slug:semesterId>/<slug:moduleId>/', views.DashboardModuleView, name="dashboard-module-views"),
    path('<slug:departementId>/<slug:semesterId>/<slug:moduleId>/Add/', views.Add_Course, name="dashboard-add-course"),
    path('<slug:departementId>/<slug:semesterId>/Add/', views.Add_Module, name="dashboard-add-module"),

]
