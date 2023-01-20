from django.urls import path, include, re_path
from django.contrib import admin
from django.conf import settings
from django.views.static import serve


urlpatterns = [
    path('admin/', admin.site.urls),

    # Portfolio
    path('', include('apps.portfolio.api.routers'), name='projects'),
    path('', include('apps.skills.api.routers'), name='skills'),
]

urlpatterns += [
    re_path(r'^media/(?P<path>.*)$', serve, {
        'document_root': settings.MEDIA_ROOT,
    }),
]

if settings.DEBUG:
    from django.conf.urls.static import static
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)