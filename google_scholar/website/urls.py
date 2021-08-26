from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('organisation/create/', views.CreateOrganisation.as_view(), name='create_organisation'),
    path('organisation/', views.ListOrganisation.as_view(), name='list_organisation')
]
