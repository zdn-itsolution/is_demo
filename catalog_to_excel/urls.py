from django.urls import path
from . import views


urlpatterns = [
    path('', views.get_form, name='catalog_download_form'),
    path('get_excel', views.get_excel, name='get_catalog_excel')
]