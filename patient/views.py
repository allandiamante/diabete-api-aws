from django.views.generic import TemplateView
from django.views.generic.edit import  CreateView, UpdateView, DeleteView
from django.views.generic.list import  ListView
from django.contrib.messages.views import SuccessMessageMixin
from django.urls import reverse_lazy
from .models import Patient, Medicine, CollectData, ExamsResult, Condition, HRVTime, HRVFreq, HRVNonLinear
# Create your views here.



class IndexView(TemplateView):
    template_name = 'index.html'



   ############################ Create ############################
class PatientCreate(SuccessMessageMixin, CreateView):
    model = Patient
    title = 'Register Patient'
    template_name = 'form.html'
    fields = ['subject_name', 'age', 
            'initials', 'gender', 'weight', 'height', 'phone',
            'state', 'city', 'bmi', 'bsa', 'smoker', 'alcohol', 
            'physical_activity', 'dm', 'type_dm', 'age_dm_diagnosis', 
            'dm_duration', 'hipo_mes', 'internacao_dm', 'sbp_repous',
            'dbp_repous', 'sbp_empe', 'dbp_empe', 'sbp_change', 
            'dbp_change', 'postural_drop', 'mean_hr', 'rr_resting', 
            'rr_db', 'rr_valsalva', 'rr_standing', 'obrienc_cs', 
            'can_status', 'brs_status', 'collected_data', 'observations']

    sucess_message = 'New Patient added sucessfully'
    success_url = reverse_lazy('ls-patient')

class MedicineCreate(CreateView):

    model = Medicine
    title = 'Register Medicine'
    template_name = 'form.html'
    fields = [ 'patient_medicines','insulin', 'ace_arb', 
    'sinvas_mg', 'atorvas_mg','rosuvas_mg', 'losartan_mg', 
    'enalapril_mg', 'quetiapina_mg','venlafaxina_mg',
        'omeprazol_mg', 'ranitidina_mg', 'carbamazpn_mg',
        'anticoncepcional', 'ass_mg', 'lt4_mg', 'collected_data',
        'mtf_mg']
    success_url = reverse_lazy('ls-medicine')
    sucess_message = 'New Medicine added sucessfully'

class ExamsResultCreate(CreateView):

    model = ExamsResult
    title = 'Register ExamsResult'
    template_name = 'form.html'
    fields = [  'patient_exams','hba1c_percent', 
    'hba1c_mmol_mol', 'hb_g_dl', 'glicemia_mg_dl',
    'glicemia_mmol_l', 'urine_albumina_mg_24h', 'microAlb',
        'creatina_mg_dl','creatina_umol_l', 'acr_alb_creat',
        'rpc_prot_creat', 'clear_creatinina','ct_mg_dl', 
        'ct_mmol_l', 'hdl_mg_dl', 'ldl_mg_dl', 'vitb12',
        'vitd', 'tsh', 'tg_mg_dl', 'tg_mmol_l' , 'na', 
        'basek', 'ureia']

    success_url = reverse_lazy('ls-examsresult')

class ConditionCreate(CreateView):

    model = Condition
    title = 'Register Condition'
    template_name = 'form.html'
    fields = ['patient_conditions','drge', 'vitiligo', 
    'doenca_celiaca', 'doenca_pulmonar','ace_arb', 'tireoide', 
    'retinopathy', 'nephropathy','peripheral_neuropathy', 'pn_symptoms',
        'pn_signs' ]
    success_url = reverse_lazy('ls-condition')

class CollectDataCreate(CreateView):

    model = CollectData
    title = 'Register CollectData'
    template_name = 'form.html'
    fields = [ 'patient_data','study', 'ecg', 
    'ppg', 'abp', 'emg', 'abspathrecord_times', 'sampling_freq_hz', 'ecg_signal',
        'device', 'observations']
    success_url = reverse_lazy('ls-collectdata')

class HRVTimeCreate(CreateView):

    model = HRVTime
    title = 'Register HRVTime'
    template_name = 'form.html'
    fields = [ 'collectdata_time','nn_mean', 
    'nn_median', 'nn_mode', 'nn_variance',
    'nn_skew', 'nn_kurt', 'nn_iqr', 'sd_nn',
    'cv', 'rmssd', 'sdsd',
    'nn50', 'pnn50_pr', 'nn20',
    'pnn20_pr', 'hr_change', 'gti',
    'tinn', 'si']
    success_url = reverse_lazy('ls-hrvtime')

class HRVFreqCreate(CreateView):

    model = HRVFreq
    title = 'Register HRVFreq'
    template_name = 'form.html'
    fields = [ 'collectdata_freq','ulf_lomb_ms2', 
    'vlf_lomb_ms2', 'lf_lomb_ms2', 'hf_lomb_ms2',
    'ulf_lomb_log', 'vlf_lomb_log', 'lf_lomb_log', 'hf_lomb_log',
    'ttlpwr_lomb_ms2', 'lf_hf_lomb', 'power_vlf_lomb',
    'power_lf_lomb', 'power_hf_lomb', 'lf_nu_lomb', 'hf_nu_lomb',
    'ulf_welch', 'vlf_welch', 'lf_welch',
    'hf_welch', 'ttlpwr_welch', 'lfhf_welch', 'power_vlf_welch',
    'power_lf_welch', 'power_hf_welch', 'lf_nu_welch', 'hf_nu_welch']
    success_url = reverse_lazy('ls-hrvfreq')


class HRVNonLinearCreate(CreateView):

    model = HRVNonLinear
    title = 'Register HRVNonLinear'
    template_name = 'form.html'
    fields = [  'collectdata_non_lin','sd1','sd2','sd1_sd2_ratio','ellipse_area','csi','cvi','alpha1',
                'alpha2','d2_10','d2_20','ent_aprox_1_01','ent_aprox_1_015',
                'ent_aprox_1_02','ent_aprox_1_025','ent_aprox_2_01','ent_aprox_2_015',
                'ent_aprox_2_02','ent_aprox_2_025','ent_amostra_1','ent_amostra_2',
                'ent_multiescala_e3','ent_multiescala_e5','ent_fuzzy','ent_shannon_1',
                'ent_shannon_2','ent_spectral','ent_permutation_1','norm_entropy',
                'ent_permutation_2','ent_conditional','ent_corrected_cond','ctm_r1',
                'ctm_r2','ctm_r3','area_sodp_rr_log','area_sodp_rr','mean_dr1','mean_dr2',
                'mean_dr3','mean_dr4','mean_dr5'    
    ]
    success_url = reverse_lazy('ls-hrvnonlin')
   

   ############################ UPDATE ############################


class PatientUpdate(SuccessMessageMixin, UpdateView):
    model = Patient
    title = 'ExamsResult'
    template_name = 'ed-form.html'
    fields = ['subject_name', 'age', 
            'initials', 'gender', 'weight', 'height', 'phone',
            'state', 'city', 'bmi', 'bsa', 'smoker', 'alcohol', 
            'physical_activity', 'dm', 'type_dm', 'age_dm_diagnosis', 
            'dm_duration', 'hipo_mes', 'internacao_dm', 'sbp_repous',
            'dbp_repous', 'sbp_empe', 'dbp_empe', 'sbp_change', 
            'dbp_change', 'postural_drop', 'mean_hr', 'rr_resting', 
            'rr_db', 'rr_valsalva', 'rr_standing', 'obrienc_cs', 
            'can_status', 'brs_status', 'collected_data', 'observations']
    success_url = reverse_lazy('ls-patient')
    sucess_message = 'New Patient added sucessfully'


class MedicineUpdate(UpdateView):

    model = Medicine
    title = 'ExamsResult'
    template_name = 'ed-form.html'
    fields = [ 'patient_medicines','insulin', 'ace_arb', 
    'sinvas_mg', 'atorvas_mg','rosuvas_mg', 'losartan_mg', 
    'enalapril_mg', 'quetiapina_mg','venlafaxina_mg',
        'omeprazol_mg', 'ranitidina_mg', 'carbamazpn_mg',
        'anticoncepcional', 'ass_mg', 'lt4_mg', 'collected_data',
        'mtf_mg']
    success_url = reverse_lazy('ls-medicine')
    sucess_message = 'New Medicine added sucessfully'

class ExamsResultUpdate(UpdateView):

    model = ExamsResult
    title = 'ExamsResult'
    template_name = 'ed-form.html'
    fields = [  'patient_exams','hba1c_percent', 
    'hba1c_mmol_mol', 'hb_g_dl', 'glicemia_mg_dl',
    'glicemia_mmol_l', 'urine_albumina_mg_24h', 'microAlb',
        'creatina_mg_dl','creatina_umol_l', 'acr_alb_creat',
        'rpc_prot_creat', 'clear_creatinina','ct_mg_dl', 
        'ct_mmol_l', 'hdl_mg_dl', 'ldl_mg_dl', 'vitb12',
        'vitd', 'tsh', 'tg_mg_dl', 'tg_mmol_l' , 'na', 
        'basek', 'ureia']
    success_url = reverse_lazy('ls-examsresult')

class ConditionUpdate(UpdateView):

    model = Condition
    title = 'ExamsResult'
    template_name = 'ed-form.html'
    fields = ['patient_conditions','drge', 'vitiligo', 
    'doenca_celiaca', 'doenca_pulmonar','ace_arb', 'tireoide', 
    'retinopathy', 'nephropathy','peripheral_neuropathy', 'pn_symptoms',
        'pn_signs']
    success_url = reverse_lazy('ls-condition')

class CollectDataUpdate(UpdateView):

    model = CollectData
    title = 'ExamsResult'
    template_name = 'ed-form.html'
    fields = [ 'patient_data','study', 'ecg', 
    'ppg', 'abp', 'emg', 'abspathrecord_times', 'sampling_freq_hz','ecg_signal',
        'device', 'observations']
    success_url = reverse_lazy('ls-collectdata')

class HRVTimeUpdate(UpdateView):

    model = HRVTime
    title = 'ExamsResult'
    template_name = 'ed-form.html'
    fields = [ 'collectdata_time','nn_mean', 
    'nn_median', 'nn_mode', 'nn_variance',
    'nn_skew', 'nn_kurt', 'nn_iqr', 'sd_nn',
    'cv', 'rmssd', 'sdsd',
    'nn50', 'pnn50_pr', 'nn20', 
    'pnn20_pr', 'hr_change', 'gti',
    'tinn', 'si']
    success_url = reverse_lazy('ls-hrvtime')

class HRVFreqUpdate(UpdateView):

    model = HRVFreq
    title = 'ExamsResult'
    template_name = 'ed-form.html'
    fields = [ 'collectdata_freq','ulf_lomb_ms2', 
    'vlf_lomb_ms2', 'lf_lomb_ms2', 'hf_lomb_ms2',
    'ulf_lomb_log', 'vlf_lomb_log', 'lf_lomb_log', 'hf_lomb_log',
    'ttlpwr_lomb_ms2', 'lf_hf_lomb', 'power_vlf_lomb',
    'power_lf_lomb', 'power_hf_lomb', 'lf_nu_lomb', 'hf_nu_lomb',
    'ulf_welch', 'vlf_welch', 'lf_welch',
    'hf_welch', 'ttlpwr_welch', 'lfhf_welch', 'power_vlf_welch',
    'power_lf_welch', 'power_hf_welch', 'lf_nu_welch', 'hf_nu_welch']
    success_url = reverse_lazy('ls-hrvfreq')

class HRVNonLinearUpdate(UpdateView):

    model = HRVNonLinear
    title = 'ExamsResult'
    template_name = 'ed-form.html'
    fields = [  'collectdata_non_lin','sd1','sd2','sd1_sd2_ratio','ellipse_area','csi','cvi','alpha1',
                'alpha2','d2_10','d2_20','ent_aprox_1_01','ent_aprox_1_015',
                'ent_aprox_1_02','ent_aprox_1_025','ent_aprox_2_01','ent_aprox_2_015',
                'ent_aprox_2_02','ent_aprox_2_025','ent_amostra_1','ent_amostra_2',
                'ent_multiescala_e3','ent_multiescala_e5','ent_fuzzy','ent_shannon_1',
                'ent_shannon_2','ent_spectral','ent_permutation_1','norm_entropy',
                'ent_permutation_2','ent_conditional','ent_corrected_cond','ctm_r1',
                'ctm_r2','ctm_r3','area_sodp_rr_log','area_sodp_rr','mean_dr1','mean_dr2',
                'mean_dr3','mean_dr4','mean_dr5'    
    ]
    success_url = reverse_lazy('ls-hrvnonlin')

       ############################ DELETE ############################


class PatientDelete(SuccessMessageMixin, DeleteView):
    model = Patient
    title = 'ExamsResult'
    template_name = 'ex-form.html'
    sucess_message = 'New Patient added sucessfully'
    success_url = reverse_lazy('ls-patient')

class MedicineDelete(DeleteView):
    model = Medicine
    title = 'ExamsResult'
    template_name = 'ex-form.html'
    sucess_message = 'New Medicine added sucessfully'
    success_url = reverse_lazy('ls-medicine')

class ExamsResultDelete(DeleteView):
    model = ExamsResult
    title = 'ExamsResult'
    template_name = 'ex-form.html'
    success_url = reverse_lazy('ls-examsresult')


class ConditionDelete(DeleteView):
    model = Condition
    title = 'ExamsResult'
    template_name = 'ex-form.html'
    success_url = reverse_lazy('ls-condition')

class CollectDataDelete(DeleteView):
    model = CollectData
    title = 'ExamsResult'
    template_name = 'ex-form.html'
    success_url = reverse_lazy('ls-collectdata')

class HRVTimeDelete(DeleteView):
    model = HRVTime
    template_name = 'ex-form.html'
    success_url = reverse_lazy('ls-hrvtime')

class HRVFreqDelete(DeleteView):
    model = HRVFreq
    title = 'ExamsResult'
    template_name = 'ex-form.html'
    success_url = reverse_lazy('ls-hrvfreq')

class HRVNonLinearDelete(DeleteView):
    model = HRVNonLinear
    template_name = 'ex-form.html'
    success_url = reverse_lazy('ls-hrvnonlin')



    


############################ LIST ############################


class PatientList(SuccessMessageMixin, ListView):
    model = Patient
    title = 'ExamsResult'
    template_name = 'patient.html'
    sucess_message = 'New Patient added sucessfully'


class MedicineList(ListView):
    model = Medicine
    title = 'ExamsResult'
    template_name = 'medicine.html'
    sucess_message = 'New Medicine added sucessfully'


class ExamsResultList(ListView):
    model = ExamsResult
    title = 'ExamsResult'
    template_name = 'examsresult.html'


class ConditionList(ListView):
    model = Condition
    title = 'ExamsResult'
    template_name = 'condition.html'


class CollectDataList(ListView):
    model = CollectData
    title = 'ExamsResult'
    template_name = 'collectdata.html'

class HRVTimeList(ListView):
    model = HRVTime
    title = 'ExamsResult'
    template_name = 'hrvtime.html'


class HRVFreqList(ListView):
    model = HRVFreq
    title = 'ExamsResult'
    template_name = 'hrvfreq.html'


class HRVNonLinearList(ListView):
    model = HRVNonLinear
    title = 'ExamsResult'
    template_name = 'hrvnonlin.html'




    