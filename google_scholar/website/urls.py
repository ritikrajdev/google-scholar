from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('organisation/create/', views.CreateOrganisation.as_view(), name='create_organisation'),
]
