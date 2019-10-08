from django.contrib import admin
from django.contrib.auth.models import Group

admin.site.unregister(Group)

admin.site.site_header = 'Dj E-Commerce Administration'
admin.site.site_title = 'Dj E-Commerce Administration'
