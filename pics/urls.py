from django.urls import include, path, re_path
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', views.index, name='index'),
    path('gallery/', views.gallery, name='gallery'),
    path('search/', views.search_results, name='search_results'),
    path('location/', views.location, name='location'),
    re_path(r'^location/(?P<location>\d+)',views.search_by_location, name='location_filter'),
]
if settings.DEBUG: urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
