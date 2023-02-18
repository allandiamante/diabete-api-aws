from django.views.generic import TemplateView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic.list import  ListView
from django.urls import reverse_lazy
from .models import Patient, Medicine, CollectData, ExamsResult, Condition, HRVTime, HRVFreq, HRVNonLinear
from .utils import ret_initials, calc_bmi, calc_raiz_q, calc_bsa, calc_sbp_dbp, calc_postural_drop, normalize_data
from django.contrib.auth.mixins import LoginRequiredMixin


class IndexView(TemplateView):
    template_name = 'index.html'



############################ Create ############################

class PatientCreate(LoginRequiredMixin, CreateView):
    login_url = reverse_lazy('login')
    model = Patient
    title = 'Register Patient'
    template_name = 'form.html'
    fields = ['collected_data','subject_name', 'age', 'gender', 'weight', 'height', 'phone',
            'state', 'city', 'smoker', 'alcohol',
            'physical_activity', 'dm', 'type_dm', 'age_dm_diagnosis', 
            'dm_duration', 'hipo_mes', 'internacao_dm', 'sbp_repous',
            'dbp_repous', 'sbp_empe', 'dbp_empe', 'mean_hr', 'rr_resting', 
            'rr_db', 'rr_valsalva', 'rr_standing', 'obrienc_cs', 
            'can_status', 'brs_status',  'observations']
   
    success_url = reverse_lazy('ls-patient')

    def form_valid(self, form):

        url = super().form_valid(form)
        self.object.initials = ret_initials(self.object.subject_name)
        self.object.bmi = calc_bmi(self.object.weight, self.object.height)
        self.object.bsa = calc_bsa(self.object.weight, self.object.height)
        self.object.sbp_change = calc_sbp_dbp(self.object.sbp_empe, self.object.sbp_repous)
        self.object.dbp_change = calc_sbp_dbp(self.object.dbp_empe, self.object.dbp_repous)
        self.object.postural_drop = calc_postural_drop(self.object.sbp_change, self.object.dbp_change)
        self.object.initials = ret_initials(self.object.subject_name)
        self.object.save()
 
        return url

class MedicineCreate(LoginRequiredMixin, CreateView):

    login_url = reverse_lazy('login')
    model = Medicine
    title = 'Register Medicine'
    template_name = 'form.html'
    fields = [ 'collected_data','patient_medicines','insulin', 'ace_arb', 
    'sinvas_mg', 'atorvas_mg','rosuvas_mg', 'losartan_mg', 
    'enalapril_mg', 'quetiapina_mg','venlafaxina_mg',
        'omeprazol_mg', 'ranitidina_mg', 'carbamazpn_mg',
        'anticoncepcional', 'aas_mg', 'lt4_mg', 
        'mtf_mg']
    success_url = reverse_lazy('ls-medicine')

class ExamsResultCreate(LoginRequiredMixin, CreateView):

    login_url = reverse_lazy('login')
    model = ExamsResult
    title = 'Register ExamsResult'
    template_name = 'form.html'
    fields = [  'collected_data', 'patient_exams','hba1c_percent', 
    'hba1c_mmol_mol', 'hb_g_dl', 'glicemia_mg_dl',
    'glicemia_mmol_l', 'urine_albumina_mg_24h', 'microAlb',
        'creatina_mg_dl','creatina_umol_l', 'acr_alb_creat',
        'rpc_prot_creat', 'clear_creatinina','ct_mg_dl', 
        'ct_mmol_l', 'hdl_mg_dl', 'ldl_mg_dl', 'vitb12',
        'vitd', 'tsh', 'tg_mg_dl', 'tg_mmol_l' , 'na', 
        'basek', 'ureia']

    success_url = reverse_lazy('ls-examsresult')

class ConditionCreate(LoginRequiredMixin, CreateView):

    login_url = reverse_lazy('login')
    model = Condition
    title = 'Register Condition'
    template_name = 'form.html'
    fields = ['collected_data','patient_conditions','drge', 'vitiligo', 
    'doenca_celiaca', 'doenca_pulmonar','ace_arb', 'tireoide', 
    'retinopathy', 'nephropathy','peripheral_neuropathy', 'pn_symptoms',
        'pn_signs' ]
    success_url = reverse_lazy('ls-condition')

class CollectDataCreate(LoginRequiredMixin, CreateView):

    login_url = reverse_lazy('login')
    model = CollectData
    title = 'Register CollectData'
    template_name = 'up-form.html'
    fields = [ 'collected_data','patient_data','study', 'ecg', 
    'ppg', 'abp', 'emg', 'abspathrecord_times', 'sampling_freq_hz', 'ecg_signal',
        'device', 'observations']
    success_url = reverse_lazy('ls-collectdata')

class HRVTimeCreate(LoginRequiredMixin, CreateView):

    login_url = reverse_lazy('login')
    model = HRVTime
    title = 'Register HRVTime'
    template_name = 'form.html'
    fields = [ 'collected_data', 'collectdata_time','nn_mean', 
    'nn_median', 'nn_mode', 'nn_variance',
    'nn_skew', 'nn_kurt', 'nn_iqr', 'sd_nn',
    'cv', 'rmssd', 'sdsd',
    'nn50', 'pnn50_pr', 'nn20',
    'pnn20_pr', 'hr_change', 'hti',
    'tinn', 'si']
    success_url = reverse_lazy('ls-hrvtime')

class HRVFreqCreate(LoginRequiredMixin, CreateView):

    login_url = reverse_lazy('login')
    model = HRVFreq
    title = 'Register HRVFreq'
    template_name = 'form.html'
    fields = [ 'collected_data','collectdata_freq','ulf_lomb_ms2', 
    'vlf_lomb_ms2', 'lf_lomb_ms2', 'hf_lomb_ms2',
    'ulf_lomb_log', 'vlf_lomb_log', 'lf_lomb_log', 'hf_lomb_log',
    'ttlpwr_lomb_ms2', 'lf_hf_lomb', 'power_vlf_lomb',
    'power_lf_lomb', 'power_hf_lomb', 'lf_nu_lomb', 'hf_nu_lomb',
    'ulf_welch', 'vlf_welch', 'lf_welch',
    'hf_welch', 'ttlpwr_welch', 'lfhf_welch', 'power_vlf_welch',
    'power_lf_welch', 'power_hf_welch', 'lf_nu_welch', 'hf_nu_welch']
    success_url = reverse_lazy('ls-hrvfreq')

class HRVNonLinearCreate(LoginRequiredMixin, CreateView):

    login_url = reverse_lazy('login')
    model = HRVNonLinear
    title = 'Register HRVNonLinear'
    template_name = 'form.html'
    fields = [  'collected_data','collectdata_non_lin','sd1','sd2','sd1_sd2_ratio','ellipse_area','csi',
                'cvi','alpha1','alpha2','d2_10','d2_20','ent_aprox_1_01','ent_aprox_1_015',
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

class PatientUpdate( LoginRequiredMixin, UpdateView):
    login_url = reverse_lazy('login')
    model = Patient
    title = 'ExamsResult'
    template_name = 'ed-form.html'
    fields = ['collected_data', 'subject_name', 'age', 
            'gender', 'weight', 'height', 'phone',
            'state', 'city',  'smoker', 'alcohol', 
            'physical_activity', 'dm', 'type_dm', 'age_dm_diagnosis', 
            'dm_duration', 'hipo_mes', 'internacao_dm', 'sbp_repous',
            'dbp_repous', 'sbp_empe', 'dbp_empe', 'sbp_change', 
            'dbp_change', 'postural_drop', 'mean_hr', 'rr_resting', 
            'rr_db', 'rr_valsalva', 'rr_standing', 'obrienc_cs', 
            'can_status', 'brs_status',  'observations']
    success_url = reverse_lazy('ls-patient')
    sucess_message = 'New Patient added sucessfully'



    def form_valid(self, form):

            url = super().form_valid(form)
            self.object.initials = ret_initials(self.object.subject_name)
            self.object.bmi = calc_bmi(self.object.weight, self.object.height)
            self.object.bsa = calc_bsa(self.object.weight, self.object.height)
            self.object.sbp_change = calc_sbp_dbp(self.object.sbp_empe, self.object.sbp_repous)
            self.object.dbp_change = calc_sbp_dbp(self.object.dbp_empe, self.object.dbp_repous)
            self.object.postural_drop = calc_postural_drop(self.object.sbp_change, self.object.dbp_change)
            self.object.initials = ret_initials(self.object.subject_name)
            self.object.save()
    
            return url

class MedicineUpdate(LoginRequiredMixin, UpdateView):

    login_url = reverse_lazy('login')
    model = Medicine
    title = 'ExamsResult'
    template_name = 'ed-form.html'
    fields = [  'collected_data', 'patient_medicines','insulin', 'ace_arb', 
    'sinvas_mg', 'atorvas_mg','rosuvas_mg', 'losartan_mg', 
    'enalapril_mg', 'quetiapina_mg','venlafaxina_mg',
        'omeprazol_mg', 'ranitidina_mg', 'carbamazpn_mg',
        'anticoncepcional', 'aas_mg', 'lt4_mg',
        'mtf_mg']
    success_url = reverse_lazy('ls-medicine')
    sucess_message = 'New Medicine added sucessfully'

class ExamsResultUpdate(LoginRequiredMixin, UpdateView):

    login_url = reverse_lazy('login')
    model = ExamsResult
    title = 'ExamsResult'
    template_name = 'ed-form.html'
    fields = [   'collected_data','patient_exams','hba1c_percent', 
    'hba1c_mmol_mol', 'hb_g_dl', 'glicemia_mg_dl',
    'glicemia_mmol_l', 'urine_albumina_mg_24h', 'microAlb',
        'creatina_mg_dl','creatina_umol_l', 'acr_alb_creat',
        'rpc_prot_creat', 'clear_creatinina','ct_mg_dl', 
        'ct_mmol_l', 'hdl_mg_dl', 'ldl_mg_dl', 'vitb12',
        'vitd', 'tsh', 'tg_mg_dl', 'tg_mmol_l' , 'na', 
        'basek', 'ureia']
    success_url = reverse_lazy('ls-examsresult')

class ConditionUpdate(LoginRequiredMixin, UpdateView):

    login_url = reverse_lazy('login')
    model = Condition
    title = 'ExamsResult'
    template_name = 'ed-form.html'
    fields = [ 'collected_data','patient_conditions','drge', 'vitiligo', 
    'doenca_celiaca', 'doenca_pulmonar','ace_arb', 'tireoide', 
    'retinopathy', 'nephropathy','peripheral_neuropathy', 'pn_symptoms',
        'pn_signs']
    success_url = reverse_lazy('ls-condition')

class CollectDataUpdate(LoginRequiredMixin, UpdateView):

    login_url = reverse_lazy('login')
    model = CollectData
    title = 'ExamsResult'
    template_name = 'ed-up-form.html'
    fields = [  'collected_data','patient_data','study', 'ecg', 
    'ppg', 'abp', 'emg', 'abspathrecord_times', 'sampling_freq_hz','ecg_signal',
        'device', 'observations']
    success_url = reverse_lazy('ls-collectdata')

class HRVTimeUpdate(LoginRequiredMixin, UpdateView):

    login_url = reverse_lazy('login')
    model = HRVTime
    title = 'ExamsResult'
    template_name = 'ed-form.html'
    fields = [  'collected_data','collectdata_time','nn_mean', 
    'nn_median', 'nn_mode', 'nn_variance',
    'nn_skew', 'nn_kurt', 'nn_iqr', 'sd_nn',
    'cv', 'rmssd', 'sdsd',
    'nn50', 'pnn50_pr', 'nn20', 
    'pnn20_pr', 'hr_change', 'hti',
    'tinn', 'si']
    success_url = reverse_lazy('ls-hrvtime')

class HRVFreqUpdate(LoginRequiredMixin, UpdateView):

    login_url = reverse_lazy('login')
    model = HRVFreq
    title = 'ExamsResult'
    template_name = 'ed-form.html'
    fields = [  'collected_data','collectdata_freq','ulf_lomb_ms2', 
    'vlf_lomb_ms2', 'lf_lomb_ms2', 'hf_lomb_ms2',
    'ulf_lomb_log', 'vlf_lomb_log', 'lf_lomb_log', 'hf_lomb_log',
    'ttlpwr_lomb_ms2', 'lf_hf_lomb', 'power_vlf_lomb',
    'power_lf_lomb', 'power_hf_lomb', 'lf_nu_lomb', 'hf_nu_lomb',
    'ulf_welch', 'vlf_welch', 'lf_welch',
    'hf_welch', 'ttlpwr_welch', 'lfhf_welch', 'power_vlf_welch',
    'power_lf_welch', 'power_hf_welch', 'lf_nu_welch', 'hf_nu_welch']
    success_url = reverse_lazy('ls-hrvfreq')

class HRVNonLinearUpdate(LoginRequiredMixin, UpdateView):

    login_url = reverse_lazy('login')
    model = HRVNonLinear
    title = 'ExamsResult'
    template_name = 'ed-form.html'
    fields = [   'collected_data','collectdata_non_lin','sd1','sd2','sd1_sd2_ratio','ellipse_area',
                'csi','cvi','alpha1','alpha2','d2_10','d2_20','ent_aprox_1_01','ent_aprox_1_015',
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

class PatientDelete( LoginRequiredMixin, DeleteView):
    login_url = reverse_lazy('login')
    model = Patient
    title = 'ExamsResult'
    template_name = 'ex-form.html'
    sucess_message = 'New Patient added sucessfully'
    success_url = reverse_lazy('ls-patient')

class MedicineDelete(LoginRequiredMixin, DeleteView):
    login_url = reverse_lazy('login')
    model = Medicine
    title = 'ExamsResult'
    template_name = 'ex-form.html'
    sucess_message = 'New Medicine added sucessfully'
    success_url = reverse_lazy('ls-medicine')

class ExamsResultDelete(LoginRequiredMixin, DeleteView):
    login_url = reverse_lazy('login')
    model = ExamsResult
    title = 'ExamsResult'
    template_name = 'ex-form.html'
    success_url = reverse_lazy('ls-examsresult')

class ConditionDelete(LoginRequiredMixin, DeleteView):
    login_url = reverse_lazy('login')
    model = Condition
    title = 'ExamsResult'
    template_name = 'ex-form.html'
    success_url = reverse_lazy('ls-condition')

class CollectDataDelete(LoginRequiredMixin, DeleteView):
    login_url = reverse_lazy('login')
    model = CollectData
    title = 'ExamsResult'
    template_name = 'ex-form.html'
    success_url = reverse_lazy('ls-collectdata')

class HRVTimeDelete(LoginRequiredMixin, DeleteView):
    login_url = reverse_lazy('login')
    model = HRVTime
    template_name = 'ex-form.html'
    success_url = reverse_lazy('ls-hrvtime')

class HRVFreqDelete(LoginRequiredMixin, DeleteView):
    login_url = reverse_lazy('login')
    model = HRVFreq
    title = 'ExamsResult'
    template_name = 'ex-form.html'
    success_url = reverse_lazy('ls-hrvfreq')

class HRVNonLinearDelete(LoginRequiredMixin, DeleteView):
    login_url = reverse_lazy('login')
    model = HRVNonLinear
    template_name = 'ex-form.html'
    success_url = reverse_lazy('ls-hrvnonlin')


############################ LIST ############################

class PatientList( LoginRequiredMixin, ListView):
    login_url = reverse_lazy('login')
    model = Patient, CollectData
    title = 'Patient'
    template_name = 'patient.html'
    sucess_message = 'New Patient added sucessfully'
    paginate_by = 10

    def get_queryset(self):

        search = self.request.GET.get('id')

        if search:
            patients = Patient.objects.filter(id=search)
        else:
            patients = Patient.objects.all()

        return patients

class MedicineList(LoginRequiredMixin, ListView):
    login_url = reverse_lazy('login')
    model = Medicine
    title = 'Medicine'
    template_name = 'medicine.html'
    sucess_message = 'New Medicine added sucessfully'
    paginate_by = 10


    def get_queryset(self):

        search = self.request.GET.get('id')

        if search:
            medicines = Medicine.objects.filter(id=search)
        else:
            medicines = Medicine.objects.all()

        return medicines

class ExamsResultList(LoginRequiredMixin, ListView):
    login_url = reverse_lazy('login')
    model = ExamsResult
    title = 'ExamsResult'
    template_name = 'examsresult.html'
    paginate_by = 10

    def get_queryset(self):

        search = self.request.GET.get('id')

        if search:
            exams_results = ExamsResult.objects.filter(id=search)
        else:
            exams_results = ExamsResult.objects.all()

        return exams_results

class ConditionList(LoginRequiredMixin, ListView):
    login_url = reverse_lazy('login')
    model = Condition
    title = 'Condition'
    template_name = 'condition.html'
    paginate_by = 10


    def get_queryset(self):

        search = self.request.GET.get('id')

        if search:
            conditions = Condition.objects.filter(id=search)
        else:
            conditions = Condition.objects.all()

        return conditions

class CollectDataList(LoginRequiredMixin, ListView):
    login_url = reverse_lazy('login')
    model = CollectData
    title = 'CollectData'
    template_name = 'collectdata.html'
    paginate_by = 10

    def get_queryset(self):

        search = self.request.GET.get('id')

        if search:
            collect_datas = CollectData.objects.filter(id=search)
        else:
            collect_datas = CollectData.objects.all()

        return collect_datas
        
class HRVTimeList(LoginRequiredMixin, ListView):
    login_url = reverse_lazy('login')
    model = HRVTime
    title = 'HRVTime'
    template_name = 'hrvtime.html'
    paginate_by = 10

    def get_queryset(self):

        search = self.request.GET.get('id')

        if search:
            hrv_times = HRVTime.objects.filter(id=search)
        else:
            hrv_times = HRVTime.objects.all()

        return hrv_times

class HRVFreqList(LoginRequiredMixin, ListView):
    login_url = reverse_lazy('login')
    model = HRVFreq
    title = 'HRVFreq'
    template_name = 'hrvfreq.html'
    paginate_by = 10

    def get_queryset(self):

        search = self.request.GET.get('id')

        if search:
            hrv_freqs = HRVFreq.objects.filter(id=search)
        else:
            hrv_freqs = HRVFreq.objects.all()

        return hrv_freqs

class HRVNonLinearList(LoginRequiredMixin, ListView):
    login_url = reverse_lazy('login')
    model = HRVNonLinear
    title = 'HRVNonLinear'
    template_name = 'hrvnonlin.html'
    paginate_by = 10

    def get_queryset(self):

        search = self.request.GET.get('id')

        if search:
            hrv_nonlinears = HRVNonLinear.objects.filter(id=search)
        else:
            hrv_nonlinears = HRVNonLinear.objects.all()

        return hrv_nonlinears

    