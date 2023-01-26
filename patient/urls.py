from django.urls import path
from django.conf import settings
from .views import IndexView 
from .views import PatientCreate, MedicineCreate, ExamsResultCreate, ConditionCreate, CollectDataCreate, HRVFreqCreate, HRVTimeCreate, HRVNonLinearCreate
from .views import PatientUpdate, MedicineUpdate, ExamsResultUpdate, ConditionUpdate, CollectDataUpdate, HRVFreqUpdate, HRVTimeUpdate, HRVNonLinearUpdate
from .views import PatientDelete, MedicineDelete, ExamsResultDelete, ConditionDelete, CollectDataDelete, HRVFreqDelete, HRVTimeDelete, HRVNonLinearDelete
from .views import PatientList, MedicineList, ExamsResultList, ConditionList, CollectDataList, HRVFreqList, HRVTimeList, HRVNonLinearList
from django.conf.urls.static import static

urlpatterns = [
    #path('endereço/', View.as_view(), name='nome-url'),


    path('', IndexView.as_view(), name='index'),


    #Path for create class
    path('patient/', PatientCreate.as_view(), name='patient'),
    path('medicine/', MedicineCreate.as_view(), name='medicine'),
    path('examsresult/', ExamsResultCreate.as_view(), name='examsresult'),
    path('condition/', ConditionCreate.as_view(), name='condition'),
    path('collectdata/', CollectDataCreate.as_view(), name='collectdata'),
    path('hrvfreq/', HRVFreqCreate.as_view(), name='hrvfreq'),
    path('hrvtime/', HRVTimeCreate.as_view(), name='hrvtime'),
    path('hrvnonlin/', HRVNonLinearCreate.as_view(), name='hrvnonlin'),

    #Path for edit class
    path('ed-patient/<int:pk>/', PatientUpdate.as_view(), name='ed-patient'),
    path('ed-medicine/<int:pk>/', MedicineUpdate.as_view(), name='ed-medicine'),
    path('ed-examsresult/<int:pk>/', ExamsResultUpdate.as_view(), name='ed-examsresult'),
    path('ed-collectdata/<int:pk>/', CollectDataUpdate.as_view(), name='ed-collectdata'),
    path('ed-condition/<int:pk>/', ConditionUpdate.as_view(), name='ed-condition'),
    path('ed-hrvtime/<int:pk>/', HRVTimeUpdate.as_view(), name='ed-hrvtime'),
    path('ed-hrvfreq/<int:pk>/', HRVFreqUpdate.as_view(), name='ed-hrvfreq'),
    path('ed-hrvnonlin/<int:pk>/', HRVNonLinearUpdate.as_view(), name='ed-hrvnonlin'),

    #Path for delete class
    path('ex-patient/<int:pk>/', PatientDelete.as_view(), name='ex-patient'),
    path('ex-medicine/<int:pk>/', MedicineDelete.as_view(), name='ex-medicine'),
    path('ex-examsresult/<int:pk>/', ExamsResultDelete.as_view(), name='ex-examsresult'),
    path('ex-collectdata/<int:pk>/', CollectDataDelete.as_view(), name='ex-collectdata'),
    path('ex-condition/<int:pk>/', ConditionDelete.as_view(), name='ex-condition'),
    path('ex-hrvtime/<int:pk>/', HRVTimeDelete.as_view(), name='ex-hrvtime'),
    path('ex-hrvfreq/<int:pk>/', HRVFreqDelete.as_view(), name='ex-hrvfreq'),
    path('ex-hrvnonlin/<int:pk>/', HRVNonLinearDelete.as_view(), name='ex-hrvnonlin'),
    
    #Path for List class
    path('ls-patient/', PatientList.as_view(), name='ls-patient'),
    path('ls-medicine/', MedicineList.as_view(), name='ls-medicine'),
    path('ls-examsresult/', ExamsResultList.as_view(), name='ls-examsresult'),
    path('ls-collectdata/', CollectDataList.as_view(), name='ls-collectdata'),
    path('ls-condition/', ConditionList.as_view(), name='ls-condition'),
    path('ls-hrvtime/', HRVTimeList.as_view(), name='ls-hrvtime'),
    path('ls-hrvfreq/', HRVFreqList.as_view(), name='ls-hrvfreq'),
    path('ls-hrvnonlin/', HRVNonLinearList.as_view(), name='ls-hrvnonlin'),


] 