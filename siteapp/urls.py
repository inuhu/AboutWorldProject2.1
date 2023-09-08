from django.conf.urls.static import static
from django.urls import path, re_path
from config import settings
from . import views


urlpatterns = [
    path('', views.index, name='main'),
    path('about/', views.about, name='about'),
    path('addpage/', views.ContriesAdd.as_view(), name='addpage'),
    path('post/<int:pk>/', views.show_post, name='post'),
    path('lamp/', views.lamp, name='lamp'),
]


urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
# urlpatterns += [re_path(r'^media/(?P<path>.*)$', serve, {'document_root': settings.MEDIA_ROOT,}),] для деплоя на серверах