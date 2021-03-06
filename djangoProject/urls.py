from django.contrib import admin

from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path('api/', include('apiPasssword.urls')),
    path('admin/', admin.site.urls),
    path('accounts/', include('allauth.urls')),
    path('', include('main.urls')),
    path('user/', include('django.contrib.auth.urls')),
    path('user/', include('main.urls')),

] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
