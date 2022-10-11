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
admin.site.register(Departement)
admin.site.register(Semester)
admin.site.register(Module)
admin.site.register(Course)

