from django.contrib import admin
from .models import (
    Departement,
    Semester,
    Module,
    Course,
)

admin.site.site_header = "FSBMCOURS BIBLIOTIQUE EN LIGNE"
admin.site.site_title = "FSBMCOURS BIBLIOTIQUE EN LIGNE ADMIN PANEL"
admin.site.index_title = "FSBMCOURS MANAGER"

# Register your models here



@admin.register(Semester)
class SemesterAdmin(admin.ModelAdmin):
    list_display = ['name', 'views']
    prepopulated_fields = {'views': ('name',)}
@admin.register(Course)
class CourseAdmin(admin.ModelAdmin):
    list_display = ['name','module', 'views']
    prepopulated_fields = {'views': ('name',)}

@admin.register(Departement)
class DepartementAdmin(admin.ModelAdmin):
    list_display = ['name', 'views', 'count']
    prepopulated_fields = {'views': ('name',)}

@admin.register(Module)
class ModuleAdmin(admin.ModelAdmin):
    list_display = ['name','semester', 'views','ispublic']
    prepopulated_fields = {'views': ('name',)}