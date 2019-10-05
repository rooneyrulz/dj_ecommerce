from django.contrib import admin

from .models import Profile, Experience, Education, Social


class ProfileAdmin(admin.ModelAdmin):
    list_display = [
        'user',
        'profession',
        'company',
        'location',
        'status',
        'created_at'
    ]


class SocialAdmin(admin.ModelAdmin):
    list_display = [
        'profile',
        'youtube',
        'twitter',
        'facebook',
        'linkedin',
        'instagram',
        'github'
    ]


admin.site.register(Profile, ProfileAdmin)
admin.site.register(Experience)
admin.site.register(Education)
admin.site.register(Social, SocialAdmin)
