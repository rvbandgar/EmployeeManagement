"""
URL configuration for tutorial project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path,include,re_path
from django.views.static import serve
from django.conf import settings
from django.conf.urls.static import static
import os


# def serve_media(request, path):
#     file_path = os.path.join(settings.MEDIA_ROOT, path)
#     return serve(request, path, document_root=settings.MEDIA_ROOT)



urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('app.urls')),
    # Source - https://stackoverflow.com/a
    # Posted by NGOGA innocent Patrick, modified by community. See post 'Timeline' for change history
    # Retrieved 2025-12-13, License - CC BY-SA 4.0

    # re_path(r'^media/(?P<path>.*)$',serve,{'document_root':settings.MEDIA_ROOT}),
    # re_path(r'^static/(?P<path>.*)$',serve,{'document_root':settings.STATIC_ROOT}),

]

# urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)


# Serve media files even when DEBUG = False
# if settings.MEDIA_URL and settings.MEDIA_ROOT:
#     urlpatterns += [
#         re_path(r'^media/(?P<path>.*)$', serve, {'document_root': settings.MEDIA_ROOT}),
#     ]

# # Serve static files (only in development if DEBUG = True, but included for safety)
# if settings.DEBUG:
#     urlpatterns += [
#         re_path(r'^static/(?P<path>.*)$', serve, {'document_root': settings.STATIC_ROOT}),
#     ]

if not settings.DEBUG:
    urlpatterns += [
        re_path(r'^media/(?P<path>.*)$', serve, {'document_root': settings.MEDIA_ROOT}),
        re_path(r'^static/(?P<path>.*)$', serve, {'document_root': settings.STATIC_ROOT}),
    ]




# Add media serving
# if settings.MEDIA_ROOT:
#     urlpatterns += [
#         path('media/<path:path>', serve_media),
#     ]
