from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls, name='admin'),
    path('registration/', include('registration.urls')),
    path('', include('website.urls')),
]
