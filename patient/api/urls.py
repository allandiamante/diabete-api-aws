from django.conf.urls import url, include
from .views import PatientsViewSet
from rest_framework.routers import DefaultRouter


router = DefaultRouter()
router.register("patient", PatientsViewSet, basename="patient")



urlpatterns = [
    url('', include(router.urls))
]
