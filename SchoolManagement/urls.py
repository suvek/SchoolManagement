"""SchoolManagement URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.8/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Add an import:  from blog import urls as blog_urls
    2. Add a URL to urlpatterns:  url(r'^blog/', include(blog_urls))
"""
from django.conf.urls import include, url
from django.contrib import admin

urlpatterns = [
    url(r'^admin/', include(admin.site.urls)),
    url(r'^$', 'school.views.home', name='home'),
    url(r'^new_class/$', 'school.views.newClass', name='newClass'),
    url(r'^new_student/$', 'school.views.newStudent', name='newStudent'),
    url(r'^detail_class/$', 'school.views.detailClass', name='detailClass'),
    url(r'^edit_class/$', 'school.views.editClass', name='editClass'),
    url(r'^confirm/$', 'school.views.confirmDelete', name='confirmDelete'),
    url(r'^delete/$', 'school.views.deleteClass', name='deleteClass'),

    url(r'^detail_student/$', 'school.views.detailStudent', name='detailStudent'),
    url(r'^edit_student/$', 'school.views.editStudent', name='editStudent'),
    url(r'^confirm_delete/$', 'school.views.confirmStudentDelete', name='confirmStudentDelete'),
    url(r'^delete-Student/$', 'school.views.deleteStudent', name='deleteStudent'),


    # url(r'^test/$', 'school.views.stud', name='stud'),


]
