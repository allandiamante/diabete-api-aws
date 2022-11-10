from django.conf.urls import url, include
from .views import PatientsViewSet, PrototipePatientsViewSet
from rest_framework.routers import DefaultRouter


router = DefaultRouter()
router.register("patient", PatientsViewSet, basename="patient")
router.register("prototipepatient", PrototipePatientsViewSet, basename="prototipepatient")



urlpatterns = [
    url('', include(router.urls))
]
