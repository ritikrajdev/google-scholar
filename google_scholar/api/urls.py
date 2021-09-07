from . import views
from django.urls import include, path
from rest_framework.routers import DefaultRouter


router = DefaultRouter()
router.register(r'users', views.UserViewSet, basename='user')
router.register(r'organisations', views.OrganisationViewSet, basename='organisation')
router.register(r'scholars', views.ScholarViewSet, basename='scholar')
router.register(r'papers', views.UserViewSet, basename='paper')

urlpatterns = [
    path('', include(router.urls))
]

