from django.contrib import admin
from .models import Patient, Medicines,ExamsResults, CollectData, Conditions, HRVTime, HRVFreq

admin.site.register(Patient)
admin.site.register(Conditions)
admin.site.register(Medicines)
admin.site.register(ExamsResults)
admin.site.register(CollectData)
admin.site.register(HRVTime)
admin.site.register(HRVFreq)
