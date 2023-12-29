from django.urls import path
from . import views


urlpatterns = [
    path('', views.upload_form, name='upload_from_google'),
]