from django.contrib import admin
from django.urls import path, include
from home import views

# Django admin header customization
admin.site.site_header = "Admin Panel"
admin.site.site_title = "Welcome to the admin panel"
admin.site.index_title = "Welcome to the portal" 
urlpatterns = [
    path('',views.home, name='home'),
    path('about',views.about, name='about'),
    path('projects',views.projects, name='projects'),
    path('contact',views.contact, name='contact')

]