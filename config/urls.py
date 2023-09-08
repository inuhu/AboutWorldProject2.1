from django.contrib import admin
from django.urls import path, include


urlpatterns = [
    path('', include('siteapp.urls')),
    path('admin/', admin.site.urls),
]

handler404 = "siteapp.views.handling_404"