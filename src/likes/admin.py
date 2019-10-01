from django.contrib import admin

from .models import Like


class LikeAdmin(admin.ModelAdmin):
    list_display = ['user', 'product']


admin.site.register(Like, LikeAdmin)
