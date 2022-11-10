from rest_framework import serializers
from patient.models import Patient


class PatientsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Patient
        fields = ['id', 'subject_name', 'age', 'initials', 'gender', 'weight', 'height', 'phone', 'state', 'city', 'bmi', 'bsa', 'smoker', 'alcohol', 'atividade_fisica', 'dm', 'type_dm', 'age_dm_diagnosis', 'dm_duration', 'hipo_mes', 'internacao_dm', 'sbp_repous', 'dbp_repous', 'sbp_empe', 'dbp_empe', 'sbp_change', 'dbp_change', 'postural_drop', 'mean_hr', 'rr_resting', 'rr_db', 'rr_valsalva', 'rr_standing', 'obrienc_cs', 'can_status', 'brs_status', 'collected_data', 'observations']

class PrototipePatientsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Patient
        fields = ['id', 'subject_name', 'age', 'initials']

