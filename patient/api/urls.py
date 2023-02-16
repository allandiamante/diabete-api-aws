from django.conf.urls import url, include
from django.urls import path
from drf_spectacular.views import SpectacularAPIView, SpectacularRedocView, SpectacularSwaggerView
from .views import PatientsViewSet, PrototipePatientsViewSet, MedicinesViewSet, ExamsResultsViewSet, CollectDataViewSet, ConditionsViewSet, HRVTimeViewSet, HRVFreqViewSet, HRVNonLinearViewSet
from rest_framework.routers import DefaultRouter
from rest_framework.documentation import include_docs_urls
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView


router = DefaultRouter()
#router.register("prototipepatient", PrototipePatientsViewSet, basename="prototipepatient")
router.register("patient", PatientsViewSet, basename="patient")
router.register("medicine", MedicinesViewSet, basename="medicine")
router.register("examsresult", ExamsResultsViewSet, basename="examsresult")
router.register("collectdata", CollectDataViewSet, basename="collectdata")
router.register("condition", ConditionsViewSet, basename="condition")
router.register("hrvtime", HRVTimeViewSet, basename="hrvtime")
router.register("hrvfreq", HRVFreqViewSet, basename="hrvfreq")
router.register("hrvnonlin", HRVNonLinearViewSet, basename="hrvnonlin")


urlpatterns = [
    path('schema/', SpectacularAPIView.as_view(), name='schema'),
    path('doc/', SpectacularSwaggerView.as_view(url_name='schema'), name='swagger-ui'),
    path('redoc/', SpectacularRedocView.as_view(url_name='schema'), name='redoc-ui'),
    path('token/', TokenObtainPairView.as_view()),
    path('token/refresh', TokenRefreshView.as_view()),
    url('', include(router.urls)),
]

