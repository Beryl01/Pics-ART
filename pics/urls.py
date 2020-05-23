from django.urls import include, path, re_path
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', views.index, name='index'),
    path('gallery/', views.gallery, name='gallery'),
    path('search/', views.search_results, name='search_results'),
    path('location/', views.location, name='location'),

]

