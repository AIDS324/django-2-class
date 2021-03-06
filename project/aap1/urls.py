from django.urls import path
from . import views

urlpatterns = [
    path('aap1', views.aap1,name="aap1"),
]