from django.conf import settings
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('', include('pages.urls')),
    path('products/', include('products.urls')),
    path('cart/', include('cart.urls')),
    path('users/', include('users.urls')),
    path('profiles/', include('profiles.urls')),
    path('admin/', admin.site.urls),
]

if settings.DEBUG:
    from django.conf.urls.static import static

    urlpatterns += static(
        settings.STATIC_URL,
        document_root=settings.STATIC_ROOT
    )
    urlpatterns += static(
        settings.MEDIA_URL,
        document_root=settings.MEDIA_ROOT
    )
