from django.contrib import admin
from .models import Patient, Medicines,ExamsResults, CollectData, Conditions

admin.site.register(Patient)
admin.site.register(Conditions)
admin.site.register(Medicines)
admin.site.register(ExamsResults)
admin.site.register(CollectData)
