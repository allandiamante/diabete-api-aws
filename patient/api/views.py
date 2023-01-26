from rest_framework import viewsets
from rest_framework.response import Response
from patient.models import Patient, Medicine, CollectData, ExamsResult, Condition, HRVTime, HRVFreq, HRVNonLinear
from .serializer import PatientsSerializer, PrototipePatientsSerializer, MedicinesSerializer, ExamsResultsSerializer, CollectDataSerializer, ConditionsSerializer, HRVFreqSerializer, HRVTimeSerializer, HRVNonLinearSerializer


#TIRAR DUVIDA
#O "height" DEVE SER INT OU FLOAT
#Como IBM será uma variavel calculada, deve-se tirar do formulário? * Tratar erros 
#calcular initials

def ret_initials(subject_name):  
    remover_palavras  = ['da', 'de', 'do' ]
    lista_frase = subject_name.split()
    result = [palavra for palavra in lista_frase if palavra.lower() not in remover_palavras]
    retorno = ' '.join(result)
    subject_name = retorno.split(' ')
    initials = ''
    for i in subject_name:
        initials = initials + i[0].upper()
    print(initials)
    return initials

def calc_bmi(weight, height):
    return (weight / (height * height) ) 

def calc_raiz_q(x):
    return x ** (1/2)

def calc_bsa(weight, height):
    cm = 100
    return calc_raiz_q((height * cm ) * weight / 3600)

def calc_sbp_dbp(empe, repous):
    return (empe - repous)

def calc_postural_drop(sbp_chambe, dbp_chambe):
    if(sbp_chambe > 20 or dbp_chambe > 10):
        return True
    else:
        return False


class PatientsViewSet(viewsets.ModelViewSet):
    serializer_class = PatientsSerializer


    def get_queryset(self):
        patients = Patient.objects.all()
        return patients   

    def create(self, request, *args, **kwargs):
        data = request.data

        new_patient = Patient.objects.create(
            subject_name=data["subject_name"], age=data['age'], 
            initials=ret_initials(data["subject_name"]), #Calculated   
             gender=data["gender"], weight=data["weight"], height=data["height"], phone=data["phone"],
              state=data["state"], city=data["city"],             
              bmi=calc_bmi(data["weight"], data["height"]), #Calculated     
               bsa=calc_bsa(data["weight"], data["height"]), #Calculated
               smoker=data["smoker"],alcohol=data["alcohol"], physical_activity=data["physical_activity"], dm=data["dm"], type_dm=data["type_dm"],
                age_dm_diagnosis=data["age_dm_diagnosis"], dm_duration=data["dm_duration"], hipo_mes=data["hipo_mes"],
                 internacao_dm=data["internacao_dm"], sbp_repous=data["sbp_repous"], dbp_repous=data["dbp_repous"],
                  sbp_empe=data["sbp_empe"], dbp_empe=data["dbp_empe"],
                   sbp_change=calc_sbp_dbp(data["sbp_empe"], data["sbp_repous"]), #Calculated     
                   dbp_change=calc_sbp_dbp(data["dbp_empe"], data["dbp_repous"]), #Calculated     
                    postural_drop=calc_postural_drop(calc_sbp_dbp(data["sbp_empe"], data["sbp_repous"]), calc_sbp_dbp(data["dbp_empe"], data["dbp_repous"])), #Calculated     
                     mean_hr=data["mean_hr"], rr_resting=data["rr_resting"], rr_db=data["rr_db"], rr_valsalva=data["rr_valsalva"],
                     rr_standing=data["rr_standing"], obrienc_cs=data["obrienc_cs"], can_status=data["can_status"],
                      brs_status=data["brs_status"], collected_data=data["collected_data"], observations=data["observations"])
    
        new_patient.save()  
        serializer = PatientsSerializer(new_patient)
        return Response(serializer.data)

    # def get_context_data(self, **kwargs):
    #     context = super().get_context_data(**kwargs)
    #     context['']
    #     return context

class MedicinesViewSet(viewsets.ModelViewSet):
    serializer_class = MedicinesSerializer

    def get_queryset(self):
        medicines = Medicines.objects.all()
        return medicines

    def create(self, request, *args, **kwargs):
        data = request.data
        new_medicines = Medicines.objects.create(
            collected_data=data["collected_data"],
            patient_medicines=Patient.objects.get(pk=int(data["patient_medicines"])),
             insulin=data['insulin'], ace_arb=data["ace_arb"], sinvas_mg=data["sinvas_mg"], atorvas_mg=data["atorvas_mg"],
              rosuvas_mg=data["rosuvas_mg"], losartan_mg=data["losartan_mg"], enalapril_mg=data["enalapril_mg"],
               quetiapina_mg=data["quetiapina_mg"], venlafaxina_mg=data["venlafaxina_mg"], omeprazol_mg=data["omeprazol_mg"],
                ranitidina_mg=data["ranitidina_mg"], carbamazpn_mg=data["carbamazpn_mg"], anticoncepcional=data["anticoncepcional"],
                 ass_mg=data["ass_mg"], lt4_mg=data["lt4_mg"], mtf_mg=data["mtf_mg"])

        new_medicines.save() 
        serializer = MedicinesSerializer(new_medicines)
        return Response(serializer.data)

class ExamsResultsViewSet(viewsets.ModelViewSet):
    serializer_class = ExamsResultsSerializer

    def get_queryset(self):
        examsresults = ExamsResults.objects.all()
        return examsresults

    def create(self, request, *args, **kwargs):
        data = request.data
        new_examsresults = ExamsResults.objects.create(
            collected_data=data["collected_data"],
            patient_exams=Patient.objects.get(pk=int(data["patient_exams"])),
             hba1c_percent=data['hba1c_percent'], hba1c_mmol_mol=data["hba1c_mmol_mol"], hb_g_dl=data["hb_g_dl"], glicemia_mg_dl=data["glicemia_mg_dl"],
              glicemia_mmol_l=data["glicemia_mmol_l"], urine_albumina_mg_24h=data["urine_albumina_mg_24h"], microAlb=data["microAlb"],
               creatina_mg_dl=data["creatina_mg_dl"], creatina_umol_l=data["creatina_umol_l"], acr_alb_creat=data["acr_alb_creat"],
                rpc_prot_creat=data["rpc_prot_creat"], clear_creatinina=data["clear_creatinina"], ct_mg_dl=data["ct_mg_dl"],
                 ct_mmol_l=data["ct_mmol_l"], hdl_mg_dl=data["hdl_mg_dl"], ldl_mg_dl=data["ldl_mg_dl"],
                 vitb12=data["vitb12"], vitd=data["vitd"], tsh=data["tsh"],
                 tg_mg_dl=data["tg_mg_dl"], tg_mmol_l=data["tg_mmol_l"], na=data["na"],
                 basek=data["basek"], ureia=data["ureia"])

        new_examsresults.save() 
        serializer = ExamsResultsSerializer(new_examsresults)
        return Response(serializer.data)

class CollectDataViewSet(viewsets.ModelViewSet):
    serializer_class = CollectDataSerializer

    def get_queryset(self):
        examsresults = CollectData.objects.all()
        return examsresults

    def create(self, request, *args, **kwargs):
        data = request.data
        new_collectdata = CollectData.objects.create(
            collected_data=data["collected_data"],
            patient_data=Patient.objects.get(pk=int(data["patient_data"])),
             study=data['study'], ecg=data["ecg"], ppg=data["ppg"], abp=data["abp"], emg = data["emg"], 
              abspathrecord_times=data["abspathrecord_times"], sampling_freq_hz=data["sampling_freq_hz"],  ecg_signal=data["ecg_signal"],
               device=data["device"], observations=data["observations"])

        new_collectdata.save() 
        serializer = CollectDataSerializer(new_collectdata)
        return Response(serializer.data)

class ConditionsViewSet(viewsets.ModelViewSet):      

    serializer_class = ConditionsSerializer

    def get_queryset(self):
        conditions = Conditions.objects.all()
        return conditions

    def create(self, request, *args, **kwargs):
        data = request.data
        new_conditions = Conditions.objects.create(
            collected_data=data["collected_data"],
            patient_conditions=Patient.objects.get(pk=int(data["patient_conditions"])),
             drge=data['drge'], vitiligo=data["vitiligo"], doenca_celiaca=data["doenca_celiaca"],
              doenca_pulmonar=data["doenca_pulmonar"], ace_arb=data["ace_arb"], tireoide=data["tireoide"],
               retinopathy=data["retinopathy"], nephropathy=data["nephropathy"], peripheral_neuropathy=data["peripheral_neuropathy"],
                pn_symptoms=data["pn_symptoms"], pn_signs=data["pn_signs"])

        new_conditions.save() 
        serializer = ConditionsSerializer(new_conditions)
        return Response(serializer.data)

class HRVTimeViewSet(viewsets.ModelViewSet):
    serializer_class = HRVTimeSerializer

    def get_queryset(self):
        examsresults = HRVTime.objects.all()
        return examsresults

    def create(self, request, *args, **kwargs):
        data = request.data
        new_hrvtime = HRVTime.objects.create(
            collected_data=data["collected_data"],
            collectdata_time=CollectData.objects.get(pk=int(data["collectdata_time"])),
             nn_mean=data['nn_mean'], nn_median=data["nn_median"], nn_mode=data["nn_mode"], nn_variance=data["nn_variance"],
              nn_skew=data["nn_skew"], nn_kurt=data["nn_kurt"], nn_iqr=data["nn_iqr"],
               sd_nn=data["sd_nn"], cv=data["cv"], rmssd=data["rmssd"],
                sdsd=data["sdsd"],nn50=data["nn50"], pnn50_pr=data["pnn50_pr"], nn20=data["nn20"],
                pnn20_pr=data["pnn20_pr"], hr_change=data["hr_change"], gti=data["gti"],
                tinn=data["tinn"], si=data["si"])

        new_hrvtime.save() 
        serializer = HRVTimeSerializer(new_hrvtime)
        return Response(serializer.data)

class HRVFreqViewSet(viewsets.ModelViewSet):
    serializer_class = HRVFreqSerializer

    def get_queryset(self):
        examsresults = HRVFreq.objects.all()
        return examsresults

    def create(self, request, *args, **kwargs):
        data = request.data
        new_hrvfreq = HRVFreq.objects.create(
            collected_data=data["collected_data"],
            collectdata_freq=CollectData.objects.get(pk=int(data["collectdata_freq"])),
             ulf_lomb_ms2=data['ulf_lomb_ms2'], vlf_lomb_ms2=data["vlf_lomb_ms2"], lf_lomb_ms2=data["lf_lomb_ms2"], 
              hf_lomb_ms2=data["hf_lomb_ms2"], ulf_lomb_log=data["ulf_lomb_log"],
               vlf_lomb_log=data["vlf_lomb_log"],lf_lomb_log=data["lf_lomb_log"], 
                hf_lomb_log=data["hf_lomb_log"], ttlpwr_lomb_ms2=data["ttlpwr_lomb_ms2"],
                 lf_hf_lomb=data["lf_hf_lomb"],                 
                 power_vlf_lomb=data['power_vlf_lomb'], power_lf_lomb=data["power_lf_lomb"], power_hf_lomb=data["power_hf_lomb"], 
                  lf_nu_lomb=data["lf_nu_lomb"], hf_nu_lomb=data["hf_nu_lomb"],
                  ulf_welch=data["ulf_welch"],vlf_welch=data["vlf_welch"], 
                  lf_welch=data["lf_welch"], hf_welch=data["hf_welch"],
                    ttlpwr_welch=data["ttlpwr_welch"],                 
                      lfhf_welch=data['lfhf_welch'], power_vlf_welch=data["power_vlf_welch"], power_lf_welch=data["power_lf_welch"], 
                      power_hf_welch=data["power_hf_welch"], lf_nu_welch=data["lf_nu_welch"],
                      hf_nu_welch=data["hf_nu_welch"])
    
        new_hrvfreq.save() 
        serializer = HRVFreqSerializer(new_hrvfreq)
        return Response(serializer.data)

class HRVNonLinearViewSet(viewsets.ModelViewSet):
    serializer_class = HRVNonLinearSerializer

    def get_queryset(self):
        examsresults = HRVNonLinear.objects.all()
        return examsresults

    def create(self, request, *args, **kwargs):
        data = request.data
        new_hrvnonlinear = HRVNonLinear.objects.create(
            collected_data=data["collected_data"],
            collectdata_non_lin=CollectData.objects.get(pk=int(data["collectdata_non_lin"])),
            sd1 = data['sd1'], sd2 = data['sd2'], sd1_sd2_ratio = data['sd1_sd2_ratio'],
             ellipse_area = data['ellipse_area'], csi = data['csi'], cvi = data['cvi'],
              alpha1 = data['alpha1'], alpha2 = data['alpha2'], d2_10 = data['d2_10'],
               d2_20 = data['d2_20'], ent_aprox_1_01 = data['ent_aprox_1_01'], ent_aprox_1_015 = data['ent_aprox_1_015'],
                ent_aprox_1_02 = data['ent_aprox_1_02'], ent_aprox_1_025 = data['ent_aprox_1_025'], ent_aprox_2_01 = data['ent_aprox_2_01'],
                 ent_aprox_2_015 = data['ent_aprox_2_015'], ent_aprox_2_02 = data['ent_aprox_2_02'], ent_aprox_2_025 = data['ent_aprox_2_025'], 
                 ent_amostra_1 = data['ent_amostra_1'], ent_amostra_2 = data['ent_amostra_2'],
                  ent_multiescala_e3 = data['ent_multiescala_e3'], ent_multiescala_e5 = data['ent_multiescala_e5'], 
                  ent_fuzzy = data['ent_fuzzy'], ent_shannon_1 = data['ent_shannon_1'], ent_shannon_2 = data['ent_shannon_2'],
                   ent_spectral = data['ent_spectral'], ent_permutation_1 = data['ent_permutation_1'], norm_entropy = data['norm_entropy'],
                    ent_permutation_2 = data['ent_permutation_2'], ent_conditional = data['ent_conditional'],
                     ent_corrected_cond = data['ent_corrected_cond'], ctm_r1 = data['ctm_r1'], ctm_r2 = data['ctm_r2'], 
                     ctm_r3 = data['ctm_r3'], area_sodp_rr_log = data['area_sodp_rr_log'], area_sodp_rr = data['area_sodp_rr'],
                      mean_dr1 = data['mean_dr1'], mean_dr2 = data['mean_dr2'], mean_dr3 = data['mean_dr3'], mean_dr4 = data['mean_dr4'], mean_dr5 = data['mean_dr5'])
            
            
        new_hrvnonlinear.save() 
        serializer = HRVNonLinearSerializer(new_hrvnonlinear)
        return Response(serializer.data)
           

######  Making it easier to insert into the DB
class PrototipePatientsViewSet(viewsets.ModelViewSet):
    serializer_class = PrototipePatientsSerializer

    def get_queryset(self):
        patients = Patient.objects.all()
        return patients

    def create(self, request, *args, **kwargs):
        data = request.data

        new_patient = Patient.objects.create(
            subject_name=data["subject_name"], age=data['age'], initials=data["initials"], gender= 1, weight= 300, height= 300, phone='99999-9999', state='PR', city='Prototipe-city', bmi= 100, bsa= 10, smoker=True, alcohol=True, physical_activity= 10, dm= True, type_dm= 2, age_dm_diagnosis= 100, dm_duration= 100, hipo_mes= 100, internacao_dm=True, sbp_repous=1000, dbp_repous= 1000, sbp_empe=1000, dbp_empe= 1000, sbp_change= 10, dbp_change= 10, postural_drop= True, mean_hr= 100, rr_resting=10, rr_db= 10, rr_valsalva= 10, rr_standing= 10, obrienc_cs= 10, can_status = 0,brs_status='prototipe', collected_data='prototipe', observations ='prototipe')

        new_patient.save()
     

        serializer = PrototipePatientsSerializer(new_patient)

        return Response(serializer.data)