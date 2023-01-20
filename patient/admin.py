from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import Patient, Medicine,ExamsResult, CollectData, Condition, HRVTime, HRVFreq, HRVNonLinear

#from ./api/serializer import PatientsSerializer

def calc_bmi(weight, height):
    return (weight / (height * height) ) 

def calc_raiz_q(x):
    return x ** (1/2)

def calc_bsa(weight, height):
    cm = 100
    return calc_raiz_q((height * cm ) * weight / 3600)



class PatientAdmin(admin.ModelAdmin):
    site_header = 'Register Patient'

    fieldsets = (
        ('Section 0',
        {
            'fields' : ( 'collected_data',)
        }),
        ('Section 1',
        {
            'fields' : ( 'bmi', 'subject_name',
                         'gender', 'age', 'phone',
                        'state', 'city')
        }),
         ('Section 2',
        {
            'fields' : ( 'weight', 'height',('smoker', 'alcohol'),
                        'physical_activity', 'dm', 'type_dm', 'age_dm_diagnosis', 
                        'dm_duration', 'hipo_mes', 'internacao_dm', 'sbp_repous',
                        'dbp_repous', 'sbp_empe', 'dbp_empe', 'sbp_change', 
                        'dbp_change', 'postural_drop', 'mean_hr', 'rr_resting', 
                        'rr_db', 'rr_valsalva', 'rr_standing', 'obrienc_cs', 
          )
        }),
        ('Section 3',
        {
            'fields' : ('can_status', 'brs_status', 'observations')
        }),
    )

    list_display = ('id' , 'initials')
    search_fields = ('id',)

    # def get_form(self, request, obj=None):
    #     fields = list(super(PatientAdmin, self).get_fields(request, obj))
    #     exclude_set = set()
    #     if obj:  # obj will be None on the add page, and something on change pages
    #         exclude_set.add('bmi')
    #     return [f for f in fields if f not in exclude_set]

    # def __init__(self, *arg, **kwargs, obj=None):
    #     super().__init__(*arg, **kwargs)
    #     print(self.fields)   
    
class MedicinesAdmin(admin.ModelAdmin):
    #fieldsets = [('Text', {'fields': ['patient_medicines']})]
    list_display = ('id' , 'patient_medicines')
    search_fields = ('id',)

class ExamsResultsAdmin(admin.ModelAdmin):
    list_display = ('id' , 'patient_exams')
    search_fields = ('id',)    

class ConditionsAdmin(admin.ModelAdmin):
    list_display = ('id' , 'patient_conditions')
    search_fields = ('id',)

class CollectDataAdmin(admin.ModelAdmin):
    list_display = ('id' , 'patient_data')
    search_fields = ('id',)

class HRVTimeAdmin(admin.ModelAdmin):
    list_display = ('id' , 'collectdata_time', '__str__')
    search_fields = ('id',)

class HRVFreqAdmin(admin.ModelAdmin):
    list_display = ('id', 'collectdata_freq', '__str__')
    search_fields = ('id',)

class HRVNonLinearAdmin(admin.ModelAdmin):
    list_display = ('id', 'collectdata_non_lin', '__str__')
    search_fields = ('id',)

admin.site.register(Patient, PatientAdmin)
admin.site.register(Medicine, MedicinesAdmin )
admin.site.register(ExamsResult, ExamsResultsAdmin)
admin.site.register(Condition, ConditionsAdmin)
admin.site.register(CollectData, CollectDataAdmin)
admin.site.register(HRVTime, HRVTimeAdmin)
admin.site.register(HRVFreq, HRVFreqAdmin )
admin.site.register(HRVNonLinear, HRVNonLinearAdmin )
