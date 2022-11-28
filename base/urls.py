from django.contrib import admin
from . import views
from django.urls import path, include ,re_path
from django.conf.urls.static import static, serve
from django.conf import settings

urlpatterns = [
    re_path(r'^assets/media/(?P<path>.*)$', serve, {'document_root':settings.MEDIA_ROOT}),
    re_path(r'^assets/static/(?P<path>.*)$', serve, {'document_root':settings.STATIC_ROOT}),
    path('admin/', admin.site.urls),
    path('Dashboard/',include('dashboard.urls', namespace="dashboard")),
    path('', views.indexPage, name="index"),
    path('',include('account.urls', namespace="account")),
    path('',include('course.urls', namespace="course")),
]
if settings.DEBUG :
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
