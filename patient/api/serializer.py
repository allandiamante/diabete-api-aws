from rest_framework import serializers
from patient.models import Patient, Medicines, ExamsResults, CollectData, Conditions, HRVTime, HRVFreq


class PatientsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Patient
        fields = ['id', 'subject_name', 'age', 
        'initials', 'gender', 'weight', 'height', 'phone',
         'state', 'city', 'bmi', 'bsa', 'smoker', 'alcohol', 
         'physical_activity', 'dm', 'type_dm', 'age_dm_diagnosis', 
         'dm_duration', 'hipo_mes', 'internacao_dm', 'sbp_repous',
          'dbp_repous', 'sbp_empe', 'dbp_empe', 'sbp_change', 
          'dbp_change', 'postural_drop', 'mean_hr', 'rr_resting', 
          'rr_db', 'rr_valsalva', 'rr_standing', 'obrienc_cs', 
          'can_status', 'brs_status', 'collected_data', 'observations']

class PrototipePatientsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Patient
        fields = ['id', 'subject_name', 'age', 'initials']

class MedicinesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Medicines
        fields = [ 'id', 'patient_medicines','insulin', 'ace_arb', 
        'sinvas_mg', 'atorvas_mg','rosuvas_mg', 'losartan_mg', 
        'enalapril_mg', 'quetiapina_mg','venlafaxina_mg',
         'omeprazol_mg', 'ranitidina_mg', 'carbamazpn_mg',
         'anticoncepcional', 'ass_mg', 'lt4_mg', 'collected_data',
          'mtf_mg']

class ExamsResultsSerializer(serializers.ModelSerializer):
    class Meta:
        model = ExamsResults
        fields = [ 'id', 'patient_exams','hba1c_percent', 
        'hba1c_mmol_mol', 'hb_g_dl', 'glicemia_mg_dl',
        'glicemia_mmol_l', 'urine_albumina_mg_24h', 'microAlb',
         'creatina_mg_dl','creatina_umol_l', 'acr_alb_creat',
          'rpc_prot_creat', 'clear_creatinina','ct_mg_dl', 
          'ct_mmol_l', 'hdl_mg_dl', 'ldl_mg_dl', 'vitb12',
           'vitd', 'tsh', 'tg_mg_dl', 'tg_mmol_l' , 'na', 
           'basek', 'ureia']

class CollectDataSerializer(serializers.ModelSerializer):
    class Meta:
        model = CollectData
        fields = [ 'id', 'patient_data','study', 'ecg', 
        'ppg', 'abp','abspathrecord_times', 'sampling_freq_hz',
         'device', 'ecg_processing_status',
         'ppg_processing_status', 'brs_processing_status', 
         'observations']

class ConditionsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Conditions
        fields = [ 'id', 'patient_conditions','drge', 'vitiligo', 
        'doenca_celiaca', 'doenca_pulmonar','ace_arb', 'tireoide', 
        'retinopathy', 'nephropathy','peripheral_neuropathy', 'pn_symptoms',
         'pn_signs']

class HRVTimeSerializer(serializers.ModelSerializer):
    class Meta:
        model = HRVTime
        fields = [ 'id', 'collectdata_time','nn_mean', 
        'nn_median', 'nn_mode', 'nn_variance',
        'nn_skew', 'nn_kurt', 'nn_iqr', 'sd_nn',
        'cv', 'rmssd', 'sdsd',
        'nn50', 'pnn50_pr', 'nn20', 'pnn20',
        'pnn20_pr', 'hr_change', 'gti',
        'tinn', 'si']

class HRVFreqSerializer(serializers.ModelSerializer):
    class Meta:
        model = HRVFreq
        fields = [ 'id', 'collectdata_freq','ulf_lomb_ms2', 
        'vlf_lomb_ms2', 'lf_lomb_ms2', 'hf_lomb_ms2',
        'ulf_lomb_log', 'vlf_lomb_log', 'lf_lomb_log', 'hf_lomb_log',
        'ttlpwr_lomb_ms2', 'lf_hf_lomb', 'power_vlf_lomb',
        'power_lf_lomb', 'power_hf_lomb', 'lf_nu_lomb', 'hf_nu_lomb',
        'ulf_welch', 'vlf_welch', 'lf_welch',
        'hf_welch', 'ttlpwr_welch', 'lfhf_welch', 'power_vlf_welch',
        'power_lf_welch', 'power_hf_welch', 'lf_nu_welch', 'hf_nu_welch']