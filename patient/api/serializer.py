from rest_framework import serializers
from patient.models import Patient, Medicines


class PatientsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Patient
        fields = ['id', 'subject_name', 'age', 'initials', 'gender', 'weight', 'height', 'phone', 'state', 'city', 'bmi', 'bsa', 'smoker', 'alcohol', 'physical_activity', 'dm', 'type_dm', 'age_dm_diagnosis', 'dm_duration', 'hipo_mes', 'internacao_dm', 'sbp_repous', 'dbp_repous', 'sbp_empe', 'dbp_empe', 'sbp_change', 'dbp_change', 'postural_drop', 'mean_hr', 'rr_resting', 'rr_db', 'rr_valsalva', 'rr_standing', 'obrienc_cs', 'can_status', 'brs_status', 'collected_data', 'observations']

class PrototipePatientsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Patient
        fields = ['id', 'subject_name', 'age', 'initials']




class MedicinesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Medicines
        fields = [ 'id', 'patient_medicines','insulin', 'ace_arb', 'sinvas_mg', 'atorvas_mg','rosuvas_mg', 'losartan_mg', 'enalapril_mg', 'quetiapina_mg','venlafaxina_mg', 'omeprazol_mg', 'ranitidina_mg', 'carbamazpn_mg','anticoncepcional', 'ass_mg', 'lt4_mg', 'collected_data', 'mtf_mg']

