from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('pics', views.pics, name='pics'),
    path('picm', views.picm, name='picm'),
    path('pfcs', views.pfcs, name='pfcs'),
    path('pfcm', views.pfcm, name='pfcm'),
]