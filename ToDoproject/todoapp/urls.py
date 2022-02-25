from django.urls import path,include
from .import views

from django.conf import settings
from django.contrib.auth.views import LogoutView

from rest_framework import routers
from todoapp.api import DeloViewSet
router = routers.DefaultRouter()
router.register('dela',DeloViewSet)

urlpatterns = [
    path('',views.main_page,name = 'main_page'),    #главная страница
    path('json/',views.get_data),
    path('add_data/',views.add_data),
    path('delete_data/',views.delete_data),
]
