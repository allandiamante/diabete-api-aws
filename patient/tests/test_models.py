from django.test import TestCase
from ..models import Patient, Medicine,  ExamsResult, Condition, CollectData, HRVTime, HRVFreq, HRVNonLinear, Study



# class PatientTestCase(TestCase):    
#     @classmethod
#     def setUpTestData(cls):
#         Patient.objects.create(
#         collected_data= "2022-11-25",
#         subject_name= "Estevan Caio da Silva",
#         age= 22,
#         gender= 1,
#         weight= 70.0,
#         height= 1.5,
#         phone= "(44) 55555-5555",
#         state= "PR",
#         city= "Maringá",
#         smoker= False,
#         alcohol= False,
#         physical_activity= 0,
#         dm= False,
#         type_dm= 0,
#         age_dm_diagnosis= 0,
#         dm_duration= 0,
#         hipo_mes= 0,
#         internacao_dm= False,
#         sbp_repous= 0,
#         dbp_repous= 0,
#         sbp_empe= 0,
#         dbp_empe= 0,
#         sbp_change= 0,
#         dbp_change= 0,
#         postural_drop= False,
#         mean_hr= 1,
#         rr_resting= 0.0,
#         rr_db= 0.0,
#         rr_valsalva= 0.0,
#         rr_standing= 0.0,
#         obrienc_cs= 0,
#         can_status= 0,
#         brs_status= "Test Brs Status",            
#         observations= "Test Observations"
#     )

#     def test_str_return_patient(self):
#         p1 = Patient.objects.get( subject_name= "Estevan Caio da Silva")
#         self.assertEquals(p1.__str__() ,"Patient ID: " + str(p1.id))

class ExamsResultTestCase(TestCase):    

    @classmethod
    def setUpTestData(cls):
        p1 =  Patient.objects.create(
            collected_data= "2022-11-25",subject_name= "Estevan Caio da Silva",age= 22,gender= 1,weight= 70.0,height= 1.5,phone= "(44) 55555-5555",state= "PR",city= "Maringá",smoker= False,
            alcohol= False,physical_activity= 0,dm= False,type_dm= 0,age_dm_diagnosis= 0,dm_duration= 0,hipo_mes= 0,internacao_dm= False,sbp_repous= 0,dbp_repous= 0,sbp_empe= 0,dbp_empe= 0,
            sbp_change= 0,dbp_change= 0,postural_drop= False,mean_hr= 1,rr_resting= 0.0,rr_db= 0.0,rr_valsalva= 0.0,rr_standing= 0.0,obrienc_cs= 0,can_status= 0,brs_status= "Test Brs Status",            
            observations= "Test Observations"
        )    
        
        ExamsResult.objects.create(
            patient_exams = Patient.objects.filter(id=1).first(),
            hba1c_percent = 3,
            hba1c_mmol_mol = 3,
            hb_g_dl = 3,
            glicemia_mg_dl = 3,
            glicemia_mmol_l = 3,
            urine_albumina_mg_24h = 3,
            microAlb = True,
            creatina_mg_dl = 3,
            creatina_umol_l = 3,
            acr_alb_creat = 3,
            rpc_prot_creat = 3,
            clear_creatinina = 3,
            ct_mg_dl = 3,
            ct_mmol_l = 3,
            hdl_mg_dl = 3,
            ldl_mg_dl = 3,
            vitb12 = 3,
            vitd = 3,
            tsh = 3,
            tg_mg_dl = 3,
            tg_mmol_l = 3,
            na = 3,
            basek = 3,
            ureia = 3,
            collected_data = "2023-03-06 17:29:46.000000"
        )

    def test_str_return_examsresult(self):
        er1 = ExamsResult.objects.get( id = 1 )
        self.assertEquals(er1.__str__() ,"Exams Result ID: " + str(er1.id))

class MedicineTestCase(TestCase):   

    @classmethod
    def setUpTestData(cls):
        p1 = Patient.objects.create(
            collected_data= "2022-11-25",subject_name= "Estevan Caio da Silva",age= 22,gender= 1,weight= 70.0,height= 1.5,phone= "(44) 55555-5555",state= "PR",city= "Maringá",smoker= False,
            alcohol= False,physical_activity= 0,dm= False,type_dm= 0,age_dm_diagnosis= 0,dm_duration= 0,hipo_mes= 0,internacao_dm= False,sbp_repous= 0,dbp_repous= 0,sbp_empe= 0,dbp_empe= 0,
            sbp_change= 0,dbp_change= 0,postural_drop= False,mean_hr= 1,rr_resting= 0.0,rr_db= 0.0,rr_valsalva= 0.0,rr_standing= 0.0,obrienc_cs= 0,can_status= 0,brs_status= "Test Brs Status",            
            observations= "Test Observations"
        )    
        p1.save()
        
        Medicine.objects.create(
            patient_medicines = Patient.objects.filter(id=1).first(),
            insulin = True,
            ace_arb = True,
            sinvas_mg = 100,
            atorvas_mg = 100,
            rosuvas_mg = 100,
            losartan_mg = 100,
            enalapril_mg = 100,
            quetiapina_mg = 100,
            venlafaxina_mg = 100,
            omeprazol_mg = 100,
            ranitidina_mg = 100,
            carbamazpn_mg =100,
            anticoncepcional = True,
            aas_mg = 100,
            lt4_mg = 100,
            mtf_mg = 100,
            collected_data = "2022-11-25"
        )  

    

        

        


    def test_str_return_medicine(self):
        m1 = Medicine.objects.get( id = 1 )
        self.assertEquals(m1.__str__() ,"Medicine ID: " + str(m1.id))

# class ConditionTestCase(TestCase):  
#     def setUp(self):
#         p1 = PatientTestCase.setUp(PatientTestCase)
        
#         Condition.objects.create(
#             patient_conditions = Patient.objects.get(id=1),
#             drge = True,
#             vitiligo = True,
#             doenca_celiaca = True,
#             doenca_pulmonar = True,
#             ace_arb = True,
#             tireoide = True,
#             retinopathy = True,
#             nephropathy = True,
#             peripheral_neuropathy = True,
#             pn_symptoms = "Postman",
#             pn_signs = "Postman",
#             collected_data = "2023-03-06 17:29:46.000000"
#         )

#     def test_str_return_condition(self):
#         c1 = Condition.objects.get( id = 1 )
#         self.assertEquals(c1.__str__() ,"Condition ID: " + str(c1.id))

# class CollectDataTestCase(TestCase):  

#     def setUp(self):
#         p1 = Patient.objects.create(
#         collected_data= "2022-11-25",subject_name= "Estevan Caio da Silva",age= 22,gender= 1,weight= 70.0,height= 1.5,phone= "(44) 55555-5555",state= "PR",city= "Maringá",smoker= False,
#         alcohol= False,physical_activity= 0,dm= False,type_dm= 0,age_dm_diagnosis= 0,dm_duration= 0,hipo_mes= 0,internacao_dm= False,sbp_repous= 0,dbp_repous= 0,sbp_empe= 0,dbp_empe= 0,
#         sbp_change= 0,dbp_change= 0,postural_drop= False,mean_hr= 1,rr_resting= 0.0,rr_db= 0.0,rr_valsalva= 0.0,rr_standing= 0.0,obrienc_cs= 0,can_status= 0,brs_status= "Test Brs Status",            
#         observations= "Test Observations"
#     )      
#         s1 = Study.objects.create(collected_data = "2023-03-06 17:29:46.000000" , name_study = "test")

#         CollectData.objects.create(
#             patient_data = Patient.objects.get(id=1),
#             study = Study.objects.get(id=1),
#             ecg = True,
#             ppg = True,
#             abp = True,
#             emg = True,
#             abspathrecord_times = 100,
#             sampling_freq_hz = 100,
#             device = 100,
#             observations = "postman insertion", 
#             collected_data = "2023-03-06 17:29:46.000000",
#             ecg_signal = ""
#         )

#     def test_str_return_collectdata(self):
#         cd1 = CollectData.objects.get( id = 1 )
#         self.assertEquals(cd1.__str__() ,"Collect Data ID: " + str(cd1.id))

# class HRVTimeTestCase(TestCase):  
#     def setUp(self):
#         p1 = Patient.objects.create(
#         collected_data= "2022-11-25",subject_name= "Estevan Caio da Silva",age= 22,gender= 1,weight= 70.0,height= 1.5,phone= "(44) 55555-5555",state= "PR",city= "Maringá",smoker= False,
#         alcohol= False,physical_activity= 0,dm= False,type_dm= 0,age_dm_diagnosis= 0,dm_duration= 0,hipo_mes= 0,internacao_dm= False,sbp_repous= 0,dbp_repous= 0,sbp_empe= 0,dbp_empe= 0,
#         sbp_change= 0,dbp_change= 0,postural_drop= False,mean_hr= 1,rr_resting= 0.0,rr_db= 0.0,rr_valsalva= 0.0,rr_standing= 0.0,obrienc_cs= 0,can_status= 0,brs_status= "Test Brs Status",            
#         observations= "Test Observations")      
#         s1 = Study.objects.create(collected_data = "2023-03-06 17:29:46.000000" , name_study = "test")

#         c1 = CollectData.objects.create( patient_data = Patient.objects.get(id=1), study = Study.objects.get(id=1), ecg = True, ppg = True, abp = True, emg = True, abspathrecord_times = 100, 
#             sampling_freq_hz = 100, device = 100, observations = "postman insertion",  collected_data = "2023-03-06 17:29:46.000000", ecg_signal = "")

#         HRVTime.objects.create(
#             collectdata_time= CollectData.objects.get(id=1),
#             nn_mean= 3,
#             nn_median= 3,
#             nn_mode= 3,
#             nn_variance= 3,
#             nn_skew= 3,
#             nn_kurt= 3,
#             nn_iqr= 3,
#             sd_nn= 3,
#             cv= 3,
#             rmssd= 3,
#             sdsd= 3,
#             nn50= 3,
#             pnn50_pr= 3,
#             nn20= 3,
#             pnn20_pr= 3,
#             hr_change= 3,
#             hti= 3,
#             tinn= 3,
#             si= 3,
#             collected_data=  "2023-03-06 17:29:46.000000"
#         )

#     def test_str_return_hrvtime(self):
#         hrvt1 = HRVTime.objects.get( id = 1 )
#         self.assertEquals(hrvt1.__str__() ,"HRV Time ID: " + str(hrvt1.id))

# class HRVFreqTestCase(TestCase):  
#     def setUp(self):
#         p1 = Patient.objects.create(
#             collected_data= "2022-11-25",subject_name= "Estevan Caio da Silva",age= 22,gender= 1,weight= 70.0,height= 1.5,phone= "(44) 55555-5555",state= "PR",city= "Maringá",smoker= False,
#             alcohol= False,physical_activity= 0,dm= False,type_dm= 0,age_dm_diagnosis= 0,dm_duration= 0,hipo_mes= 0,internacao_dm= False,sbp_repous= 0,dbp_repous= 0,sbp_empe= 0,dbp_empe= 0,
#             sbp_change= 0,dbp_change= 0,postural_drop= False,mean_hr= 1,rr_resting= 0.0,rr_db= 0.0,rr_valsalva= 0.0,rr_standing= 0.0,obrienc_cs= 0,can_status= 0,brs_status= "Test Brs Status",            
#             observations= "Test Observations"
#         )      
#         s1 = Study.objects.create(collected_data = "2023-03-06 17:29:46.000000" , name_study = "test")

#         c1 = CollectData.objects.create( patient_data = Patient.objects.get(id=1), study = Study.objects.get(id=1), ecg = True, ppg = True, abp = True, emg = True, abspathrecord_times = 100, 
#             sampling_freq_hz = 100, device = 100, observations = "postman insertion",  collected_data = "2023-03-06 17:29:46.000000", ecg_signal = "")

#         HRVFreq.objects.create(
#             collectdata_freq = CollectData.objects.filter(id=1).first(),
#             ulf_lomb_ms2 = 100.00 ,
#             vlf_lomb_ms2 = 100.00 ,
#             lf_lomb_ms2 = 100.00 ,
#             hf_lomb_ms2 = 100.00,
#             ulf_lomb_log = 100.00 ,
#             vlf_lomb_log = 100.00 ,
#             lf_lomb_log = 100.00 ,
#             hf_lomb_log = 100.00 ,
#             ttlpwr_lomb_ms2 = 100.00 ,
#             lf_hf_lomb = 100.00 ,
#             power_vlf_lomb = 100.00 ,
#             power_lf_lomb = 100.00 ,
#             power_hf_lomb = 100.00 ,
#             lf_nu_lomb = 100.00 ,
#             hf_nu_lomb = 100.00 ,
#             ulf_welch = 100.00 ,
#             vlf_welch = 100.00 ,
#             lf_welch = 100.00 ,
#             hf_welch = 100.00 ,
#             ttlpwr_welch = 100.00 ,
#             lfhf_welch = 100.00 ,
#             power_vlf_welch = 100.00 ,
#             power_lf_welch = 100.00 ,
#             power_hf_welch = 100.00 ,
#             lf_nu_welch = 100.00 ,
#             hf_nu_welch = 100.00 ,
#             collected_data = "2023-03-06 17:29:46.000000"
#         )

#     def test_str_return_HRVFreq(self):
#         hrvf1 = HRVFreq.objects.get( id = 1 )
#         self.assertEquals(hrvf1.__str__() ,"HRV Frequency ID: " + str(hrvf1.id))

# class HRVNonLinearTestCase(TestCase):  



#     def setUp(self):
#         p1 = Patient.objects.create(
#             collected_data= "2022-11-25",subject_name= "Estevan Caio da Silva",age= 22,gender= 1,weight= 70.0,height= 1.5,phone= "(44) 55555-5555",state= "PR",city= "Maringá",smoker= False,
#             alcohol= False,physical_activity= 0,dm= False,type_dm= 0,age_dm_diagnosis= 0,dm_duration= 0,hipo_mes= 0,internacao_dm= False,sbp_repous= 0,dbp_repous= 0,sbp_empe= 0,dbp_empe= 0,
#             sbp_change= 0,dbp_change= 0,postural_drop= False,mean_hr= 1,rr_resting= 0.0,rr_db= 0.0,rr_valsalva= 0.0,rr_standing= 0.0,obrienc_cs= 0,can_status= 0,brs_status= "Test Brs Status",            
#             observations= "Test Observations"
#         )      
#         s1 = Study.objects.create(collected_data = "2023-03-06 17:29:46.000000" , name_study = "test")

#         c1 = CollectData.objects.create( patient_data = Patient.objects.get(id=1), study = Study.objects.get(id=1), ecg = True, ppg = True, abp = True, emg = True, abspathrecord_times = 100, 
#             sampling_freq_hz = 100, device = 100, observations = "postman insertion",  collected_data = "2023-03-06 17:29:46.000000", ecg_signal = "")

#         HRVNonLinear.objects.create(
#             collectdata_non_lin = CollectData.objects.get(id=1) ,
#             sd1 = 0.333 ,
#             sd2 = 0.333 ,
#             sd1_sd2_ratio = 0.333 ,
#             ellipse_area = 0.333 ,
#             csi = 0.333 ,
#             cvi = 0.333 ,
#             alpha1 = 0.333 ,
#             alpha2 = 0.333 ,
#             d2_10 = 0.333 ,
#             d2_20 = 0.333 ,
#             ent_aprox_1_01 = 0.333 ,
#             ent_aprox_1_015 = 0.333 ,
#             ent_aprox_1_02 = 0.333 ,
#             ent_aprox_1_025 = 0.333 ,
#             ent_aprox_2_01 = 0.333 ,
#             ent_aprox_2_015 = 0.333 ,
#             ent_aprox_2_02 = 0.333 ,
#             ent_aprox_2_025 = 0.333 ,
#             ent_amostra_1 = 0.333 ,
#             ent_amostra_2 = 0.333 ,
#             ent_multiescala_e3 = 0.333 ,
#             ent_multiescala_e5 = 0.333 ,
#             ent_fuzzy = 0.333 ,
#             ent_shannon_1 = 0.333 ,
#             ent_shannon_2 = 0.333 ,
#             ent_spectral = 0.333 ,
#             ent_permutation_1 = 0.333 ,
#             norm_entropy = 0.333 ,
#             ent_permutation_2 = 0.333 ,
#             ent_conditional = 0.333 ,
#             ent_corrected_cond = 0.333 ,
#             ctm_r1 = 0.333 ,
#             ctm_r2 = 0.333 ,
#             ctm_r3 = 0.333 ,
#             area_sodp_rr_log = 0.333 ,
#             area_sodp_rr = 0.333 ,
#             mean_dr1 = 0.333 ,
#             mean_dr2 = 0.333 ,
#             mean_dr3 = 0.333 ,
#             mean_dr4 = 0.333 ,
#             mean_dr5 = 0.333 ,
#             collected_data = "2023-03-06 17:29:46.000000"
#         )

#     def test_str_return_hrvnonlinear(self):
#         hrvf1 = HRVNonLinear.objects.get( id = 1 )
#         self.assertEquals(hrvf1.__str__() ,"HRV Non Linear ID: " + str(hrvf1.id))

