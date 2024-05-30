from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from django.urls import re_path
from django.views.static import serve
from django.conf import settings

urlpatterns = [
    # Pages for everyone (even guests)
    path('', include('home.urls')),

    # User pages
    path('user/', include('user.urls')),

    # For login using all-auth (OAuth2)
    path('accounts/', include('socialplatform.urls')),

    # Moderator pages
    path('mod/', include('moderator.urls')),

    # Admin (Control) pages
    path('control/', include('control.urls')),

    # Default django admin page
    path('admin/', admin.site.urls),

    re_path(r'^media/(?P<path>.*)$', serve,{'document_root': settings.MEDIA_ROOT}),
    re_path(r'^static/(?P<path>.*)$', serve,{'document_root': settings.STATIC_ROOTER})
]

if settings.DEBUG:
    urlpatterns += static( settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)