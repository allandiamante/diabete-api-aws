from django.conf.urls import url, include
from .views import PatientsViewSet, PrototipePatientsViewSet, MedicinesViewSet, ExamsResultsViewSet, CollectDataViewSet, ConditionsViewSet, HRVTimeViewSet, HRVFreqViewSet, HRVNonLinearViewSet
from rest_framework.routers import DefaultRouter


router = DefaultRouter()
router.register("patient", PatientsViewSet, basename="patient")
router.register("prototipepatient", PrototipePatientsViewSet, basename="prototipepatient")
router.register("medicine", MedicinesViewSet, basename="medicine")
router.register("examsresult", ExamsResultsViewSet, basename="examsresult")
router.register("collectdata", CollectDataViewSet, basename="collectdata")
router.register("condition", ConditionsViewSet, basename="condition")
router.register("hrvtime", HRVTimeViewSet, basename="hrvtime")
router.register("hrvfreq", HRVFreqViewSet, basename="hrvfreq")
router.register("hrvnonlinear", HRVNonLinearViewSet, basename="hrvnonlinear")


urlpatterns = [
    url('', include(router.urls))
]
