from django.db import models
from django import forms
from django.core.validators import MaxValueValidator, MinValueValidator
from smart_selects.db_fields import ChainedForeignKey
from django.utils import timezone
from django.contrib import admin
from django.urls import reverse

#criar uma choice box dynamic para study_choices tabela CollectData ATENÇÃO
#criar uma choice box dynamic para device_choices tabela CollectData ATENÇÃO

GENDER_CHOICES = (
        ( 1, 'Male'),
        ( 2, 'Female'),
    )

DM_CHOICES = (
        ( 1, 'Tipo 1'),
        ( 2, 'Tipo 2'),
        ( 3, 'Tipo 3 Gestacional'),
    )

STUDY_CHOICES = (
        ( 1, 'DOC_SC'),
        ( 2, 'Extra_data_Prof_jan22'),
    )

DEVICE_CHOICES = (
        ( 0, 'Not_Scan'),
        ( 1, 'AFT_Scan'),
    )

STATES_CHOICES = (
  ("AC" , "Acre"),
  ("AL" , "Alagoas"),
  ("AP" , "Amapá"),
  ("AM" , "Amazonas"),
  ("BA" , "Bahia"),
  ("CE" , "Ceará"),
  ("ES" , "Espírito Santo"),
  ("GO" , "Goiás"),
  ("MA" , "Maranhão"),
  ("MT" , "Mato Grosso"),
  ("MS" , "Mato Grosso do Sul"),
  ("MG" , "Minas Gerais"),
  ("PA" , "Pará"),
  ("PB" , "Paraíba"),
  ("PR" , "Paraná"),
  ("PE" , "Pernambuco"),
  ("PI" , "Piauí"),
  ("RJ" , "Rio de Janeiro"),
  ("RN" , "Rio Grande do Norte"),
  ("RS" , "Rio Grande do Sul"),
  ("RO" , "Rondônia"),
  ("RR" , "Roraima"),
  ("SC" , "Santa Catarina"),
  ("SP" , "São Paulo"),
  ("SE" , "Sergipe"),
  ("TO" , "Tocantins")
)

#inserir o novo atributo unico de busca
#

class Patient(models.Model):
  collected_data = models.DateTimeField(verbose_name="Collected Data", default=timezone.now) 
  subject_name = models.CharField(verbose_name="Subject Name", max_length=200)
  age = models.PositiveSmallIntegerField(verbose_name="Age", validators=[MinValueValidator(0), MaxValueValidator(150)])
  initials = models.CharField(verbose_name="Initials", max_length=10) #Variavel calculada
  gender = models.PositiveSmallIntegerField(verbose_name="Gender", validators=[MinValueValidator(1), MaxValueValidator(2)], choices=GENDER_CHOICES) 
  weight = models.FloatField(verbose_name="Weight", validators=[MinValueValidator(0.0), MaxValueValidator(400.0)])
  height = models.FloatField(verbose_name="Height", validators=[MinValueValidator(0), MaxValueValidator(4)])
  phone = models.CharField(verbose_name="Phone", max_length=15, blank=True)
  state = models.CharField(verbose_name="State", max_length=2, choices = STATES_CHOICES, blank=True)
  city = models.CharField(verbose_name="City", max_length=100, blank=True)
  bmi = models.FloatField(verbose_name="Bmi",  validators=[MinValueValidator(0.0), MaxValueValidator(450.0)], default=0.0) #Variavel calculada 
  bsa = models.FloatField(verbose_name="Bsa",  validators=[MinValueValidator(0.0), MaxValueValidator(150.0)], default=0.0) #Variavel calculada
  smoker = models.BooleanField(verbose_name="Smoker", default=False)
  alcohol = models.BooleanField(verbose_name="Alcohol", default=False)
  physical_activity = models.PositiveSmallIntegerField(verbose_name="Physical Activity", validators=[MinValueValidator(0), MaxValueValidator(10)], blank=True, default=0) 
  dm = models.BooleanField(verbose_name="Dm", default=False)# habilitar a partir da relação Dm
  type_dm = models.PositiveSmallIntegerField(verbose_name="Type Dm", validators=[MinValueValidator(0), MaxValueValidator(2)],default=0)# habilitar a partir da relação Dm
  age_dm_diagnosis = models.PositiveSmallIntegerField(verbose_name="Age Dm_Diagnosis", validators=[MinValueValidator(0), MaxValueValidator(1000)],default=0)# habilitar a partir da relação Dm
  dm_duration = models.PositiveSmallIntegerField(verbose_name="Dm Duration", validators=[MinValueValidator(0), MaxValueValidator(1000)],default=0)# habilitar a partir da relação Dm
  hipo_mes = models.SmallIntegerField(verbose_name="Hipo Mes", default=0)# habilitar a partir da relação Dm
  internacao_dm = models.BooleanField(verbose_name="Internacao Dm", default=False)# habilitar a partir da relação Dm
  sbp_repous = models.PositiveSmallIntegerField(verbose_name="Sbp Repous", validators=[MinValueValidator(0), MaxValueValidator(1000)], blank=True, null=True)
  dbp_repous = models.PositiveSmallIntegerField(verbose_name="Dbp Repous", validators=[MinValueValidator(0), MaxValueValidator(1000)], blank=True, null=True)
  sbp_empe = models.PositiveSmallIntegerField(verbose_name="Sbp Empe", validators=[MinValueValidator(0), MaxValueValidator(1000)], blank=True, null=True)
  dbp_empe = models.PositiveSmallIntegerField(verbose_name="Dbp Empe", validators=[MinValueValidator(0), MaxValueValidator(1000)], blank=True, null=True)
  sbp_change = models.SmallIntegerField(verbose_name="Sbp Change", blank=True, null=True) #Variavel calculada
  dbp_change = models.SmallIntegerField(verbose_name="Dbp Change", blank=True, null=True) #Variavel calculada
  postural_drop = models.BooleanField(verbose_name="Postural Drop", blank=True, null=True) #Variavel calculada
  mean_hr = models.PositiveSmallIntegerField(verbose_name="Mean Hr", validators=[MinValueValidator(0), MaxValueValidator(1000)], blank=True, null=True)
  rr_resting = models.FloatField(verbose_name="Rr Resting",  validators=[MinValueValidator(0.0), MaxValueValidator(10.0)], blank=True, null=True)
  rr_db = models.FloatField(verbose_name="Rr Db",  validators=[MinValueValidator(0.0), MaxValueValidator(10.0)], blank=True, null=True)
  rr_valsalva = models.FloatField(verbose_name="Rr Valsalva",  validators=[MinValueValidator(0.0), MaxValueValidator(10.0)], blank=True, null=True)
  rr_standing = models.FloatField(verbose_name="Rr Standing",  validators=[MinValueValidator(0.0), MaxValueValidator(10.0)], blank=True, null=True)
  obrienc_cs = models.PositiveSmallIntegerField(verbose_name="Obrienc Cs", validators=[MinValueValidator(0), MaxValueValidator(10)], blank=True, null=True)
  can_status = models.PositiveSmallIntegerField(verbose_name="Can Status", validators=[MinValueValidator(0), MaxValueValidator(10)], blank=True, null=True)
  brs_status = models.CharField(verbose_name="Brs Status", max_length=50,  blank=True, null=True)
  observations = models.TextField(verbose_name="Observations", max_length=1000,  blank=True, null=True)

  def __str__(self):
    #return "[Paciente Iniciais: " + self.initials + " | "  + "Paciente ID: " + str(self.id)+ "]"
    return "Patient ID: " + str(self.id)

  def get_absolute_url(self):
    return reverse('patient')  

class Medicine(models.Model):
  collected_data = models.DateTimeField(verbose_name="Collected Data",default=timezone.now)
  patient_medicines = models.ForeignKey( Patient, on_delete=models.CASCADE, verbose_name="Patient Medicines")
  insulin = models.BooleanField(verbose_name="Insulin",default=False)
  ace_arb = models.BooleanField(verbose_name="Ace Arb",default=False)
  sinvas_mg = models.PositiveSmallIntegerField(verbose_name="Sinvas Mg", validators=[MinValueValidator(0), MaxValueValidator(1000)],default=0)
  atorvas_mg = models.PositiveSmallIntegerField(verbose_name="Atorvas Mg", validators=[MinValueValidator(0), MaxValueValidator(1000)],default=0)
  rosuvas_mg = models.PositiveSmallIntegerField(verbose_name="Rosuvas Mg", validators=[MinValueValidator(0), MaxValueValidator(1000)],default=0)
  losartan_mg = models.PositiveSmallIntegerField(verbose_name="Losartan Mg", validators=[MinValueValidator(0), MaxValueValidator(1000)],default=0)
  enalapril_mg = models.PositiveSmallIntegerField(verbose_name="Enalapril Mg", validators=[MinValueValidator(0), MaxValueValidator(1000)],default=0)
  quetiapina_mg = models.PositiveSmallIntegerField(verbose_name="Quetiapina Mg", validators=[MinValueValidator(0), MaxValueValidator(1000)],default=0)
  venlafaxina_mg = models.PositiveSmallIntegerField(verbose_name="Venlafaxina Mg", validators=[MinValueValidator(0), MaxValueValidator(1000)],default=0)
  omeprazol_mg = models.PositiveSmallIntegerField(verbose_name="Omeprazol Mg", validators=[MinValueValidator(0), MaxValueValidator(1000)],default=0)
  ranitidina_mg = models.PositiveSmallIntegerField(verbose_name="Ranitidina Mg", validators=[MinValueValidator(0), MaxValueValidator(1000)],default=0)
  carbamazpn_mg = models.PositiveSmallIntegerField(verbose_name="Carbamazpn Mg", validators=[MinValueValidator(0), MaxValueValidator(1000)],default=0)
  anticoncepcional = models.BooleanField(verbose_name="Anticoncepcional",default=False)
  ass_mg = models.PositiveSmallIntegerField(verbose_name="Ass Mg", validators=[MinValueValidator(0), MaxValueValidator(1000)],default=0)
  lt4_mg = models.PositiveSmallIntegerField(verbose_name="Lt4 Mg", validators=[MinValueValidator(0), MaxValueValidator(1000)],default=0)
  mtf_mg = models.PositiveSmallIntegerField(verbose_name="Mtf Mg", validators=[MinValueValidator(0), MaxValueValidator(1000)],default=0)
  observations = models.TextField(verbose_name="Observations", max_length=1000,  blank=True, null=True)
  
  def __str__(self):
    #return "[Paciente ID: " + str(self.patient_medicines.id) + " | "  + "Medicamento ID: " +  str(self.id)+ "]"
    return "Medicine ID: " + str(self.id)

  def get_absolute_url(self):
    return reverse('medicine')  

class ExamsResult(models.Model):
  collected_data = models.DateTimeField(verbose_name="Collected Data",default=timezone.now)
  patient_exams = models.ForeignKey(Patient,verbose_name="Patient Exams", on_delete=models.CASCADE)
  hba1c_percent = models.PositiveSmallIntegerField(verbose_name="Hba1C Percent", validators=[MinValueValidator(0), MaxValueValidator(1000)],default=0)
  hba1c_mmol_mol = models.PositiveSmallIntegerField(verbose_name="Hba1C Mmol_Mol", validators=[MinValueValidator(0), MaxValueValidator(1000)],default=0) #calculado
  hb_g_dl = models.PositiveSmallIntegerField(verbose_name="Hb G_Dl", validators=[MinValueValidator(0), MaxValueValidator(1000)],default=0)
  glicemia_mg_dl = models.PositiveSmallIntegerField(verbose_name="Glicemia Mg_Dl", validators=[MinValueValidator(0), MaxValueValidator(1000)],default=0)
  glicemia_mmol_l = models.PositiveSmallIntegerField(verbose_name="Glicemia Mmol_L", validators=[MinValueValidator(0), MaxValueValidator(1000)],default=0)
  urine_albumina_mg_24h = models.PositiveSmallIntegerField(verbose_name="Urine Albumina_Mg_24H", validators=[MinValueValidator(0), MaxValueValidator(1000)],default=0)
  microAlb = models.BooleanField(verbose_name="Micro Alb", default=False)
  creatina_mg_dl = models.PositiveSmallIntegerField(verbose_name="Creatina Mg_Dl", validators=[MinValueValidator(0), MaxValueValidator(1000)],default=0)
  creatina_umol_l = models.PositiveSmallIntegerField(verbose_name="Creatina Umol_L", validators=[MinValueValidator(0), MaxValueValidator(1000)],default=0)
  acr_alb_creat = models.PositiveSmallIntegerField(verbose_name="Acr Alb_Creat", validators=[MinValueValidator(0), MaxValueValidator(1000)],default=0)
  rpc_prot_creat = models.PositiveSmallIntegerField(verbose_name="Rpc Prot_Creat", validators=[MinValueValidator(0), MaxValueValidator(1000)],default=0)
  clear_creatinina = models.PositiveSmallIntegerField(verbose_name="Clear Creatinina", validators=[MinValueValidator(0), MaxValueValidator(1000)],default=0)
  ct_mg_dl = models.PositiveSmallIntegerField(verbose_name="Ct Mg_Dl", validators=[MinValueValidator(0), MaxValueValidator(1000)],default=0)
  ct_mmol_l = models.PositiveSmallIntegerField(verbose_name="Ct Mmol_L", validators=[MinValueValidator(0), MaxValueValidator(1000)],default=0)
  hdl_mg_dl = models.PositiveSmallIntegerField(verbose_name="Hdl Mg_Dl", validators=[MinValueValidator(0), MaxValueValidator(1000)],default=0)
  ldl_mg_dl = models.PositiveSmallIntegerField(verbose_name="Ldl Mg_Dl", validators=[MinValueValidator(0), MaxValueValidator(1000)],default=0)
  vitb12 = models.PositiveSmallIntegerField(verbose_name="Vit B12", validators=[MinValueValidator(0), MaxValueValidator(1000)],default=0)
  vitd = models.PositiveSmallIntegerField(verbose_name="Vit D", validators=[MinValueValidator(0), MaxValueValidator(1000)],default=0)
  tsh = models.PositiveSmallIntegerField(verbose_name="Tsh", validators=[MinValueValidator(0), MaxValueValidator(1000)],default=0)
  tg_mg_dl = models.PositiveSmallIntegerField(verbose_name="Tg Mg_Dl", validators=[MinValueValidator(0), MaxValueValidator(1000)],default=0)
  tg_mmol_l = models.PositiveSmallIntegerField(verbose_name="Tg Mmol_L", validators=[MinValueValidator(0), MaxValueValidator(1000)],default=0)
  na = models.PositiveSmallIntegerField(verbose_name="Na", validators=[MinValueValidator(0), MaxValueValidator(1000)],default=0)
  basek = models.PositiveSmallIntegerField(verbose_name="Basek", validators=[MinValueValidator(0), MaxValueValidator(1000)],default=0)
  ureia = models.PositiveSmallIntegerField(verbose_name="Ureia", validators=[MinValueValidator(0), MaxValueValidator(1000)],default=0)

  def __str__(self):
    #return "[Paciente ID: " + str(self.patient_exams.id) + " | "  + "Resultado Exame ID: " +str(self.id)+ "]"
    return "Exams Result ID: " +str(self.id)

class Condition(models.Model):
  collected_data = models.DateTimeField(verbose_name="Collected Data", default=timezone.now)
  patient_conditions = models.OneToOneField(Patient, verbose_name="Patient Conditions",on_delete=models.CASCADE)
  drge = models.BooleanField(verbose_name="Drge", default=False)
  vitiligo = models.BooleanField(verbose_name="Vitiligo", default=False)
  doenca_celiaca = models.BooleanField(verbose_name="Doenca Celiaca", default=False)
  doenca_pulmonar = models.BooleanField(verbose_name="Doenca Pulmonar", default=False)
  ace_arb = models.BooleanField(verbose_name="Ace Arb", default=False)
  tireoide = models.BooleanField(verbose_name="Tireoide", default=False)
  retinopathy = models.BooleanField(verbose_name="Retinopathy", default=False)
  nephropathy = models.BooleanField(verbose_name="Nephropathy", default=False)
  peripheral_neuropathy = models.BooleanField(verbose_name="Peripheral Neuropathy", default=False)
  pn_symptoms = models.CharField(verbose_name="Pn Symptoms", max_length=200)
  pn_signs = models.CharField(verbose_name="Pn Signs", max_length=200)

  def __str__(self):
    #return "[Paciente ID: " + str(self.patient_conditions.id) + " | "  + "Condições ID: " + str(self.id)+ "]"
    return "Condition ID: " + str(self.id)

class CollectData(models.Model):
  collected_data = models.DateTimeField(verbose_name="Collected Data", default=timezone.now) #será uma classe futuramente, não ha necessidade
  patient_data = models.ForeignKey(Patient, verbose_name="Patient Data",  on_delete=models.CASCADE)
  study = models.PositiveSmallIntegerField(verbose_name="Study", validators=[MinValueValidator(1), MaxValueValidator(10)], choices=STUDY_CHOICES)
  ecg = models.BooleanField(verbose_name="Ecg", default=False, null=True)
  ppg = models.BooleanField(verbose_name="Ppg", default=False, null=True)
  abp = models.BooleanField(verbose_name="Abp", default=False, null=True)
  emg = models.BooleanField(verbose_name="Emg", default=False, null=True) #NOVO CAMPO
  abspathrecord_times = models.PositiveSmallIntegerField(verbose_name="Abspathrecord Times", validators=[MinValueValidator(0), MaxValueValidator(1000)],default=0, null=True)
  sampling_freq_hz = models.PositiveSmallIntegerField(verbose_name="Sampling Freq_Hz", validators=[MinValueValidator(0), MaxValueValidator(1000)],default=0, null=True)
  device = models.PositiveSmallIntegerField(verbose_name="Device", validators=[MinValueValidator(0), MaxValueValidator(1000)],default=0, null=True)
  ecg_signal = models.FileField(verbose_name="Ecg Signal (.txt)", upload_to="txt/",blank=True, null=True) # limita apenas TXT
  observations = models.TextField(verbose_name="Observations", max_length=1000, blank=True, null=True)

  def __str__(self):
    #return "[Paciente ID: " + str(self.patient_data.id) + " | "  + "Dados Coletado ID: " + str(self.id)+ "]"
    return "Collect Data ID: " + str(self.id)

class HRVTime(models.Model):
  collected_data = models.DateTimeField(default=timezone.now) #será uma classe futuramente, não ha necessidade
  collectdata_time = models.OneToOneField(        CollectData, on_delete=models.CASCADE)
  nn_mean = models.FloatField(null=True, blank=True)
  nn_median = models.FloatField(null=True, blank=True)
  nn_mode = models.FloatField(null=True, blank=True)
  nn_variance = models.FloatField(null=True, blank=True)
  nn_skew = models.FloatField(null=True, blank=True)
  nn_kurt = models.FloatField(null=True, blank=True)
  nn_iqr = models.FloatField(null=True, blank=True)
  sd_nn = models.FloatField(null=True, blank=True)
  cv = models.FloatField(null=True, blank=True)
  rmssd = models.FloatField(null=True, blank=True)
  sdsd = models.FloatField(null=True, blank=True)
  nn50 = models.FloatField(null=True, blank=True)
  pnn50_pr = models.FloatField(null=True, blank=True)
  nn20 = models.FloatField(null=True, blank=True)
  pnn20_pr = models.FloatField(null=True, blank=True)
  hr_change = models.FloatField(null=True, blank=True)
  hti = models.FloatField(null=True, blank=True)
  tinn = models.FloatField(null=True, blank=True)
  si = models.FloatField(null=True, blank=True)


  def __str__(self):
    #return "[Paciente ID: " + str(self.collectdata_time.patient_data.id) + " | " + "Dados Coletado ID: " + str(self.collectdata_time.id) + " | " + "HRV Time ID: " + str(self.id)+ "]"
    return "HRV Time ID: " + str(self.id)

class HRVFreq(models.Model):
  collected_data = models.DateTimeField(default=timezone.now) #será uma classe futuramente, não ha necessidade
  collectdata_freq = models.OneToOneField(        CollectData, on_delete=models.CASCADE)
  ulf_lomb_ms2 = models.FloatField(null=True)
  vlf_lomb_ms2 = models.FloatField(null=True)
  lf_lomb_ms2 = models.FloatField(null=True)
  hf_lomb_ms2 = models.FloatField(null=True)
  ulf_lomb_log = models.FloatField(null=True)
  vlf_lomb_log = models.FloatField(null=True)
  lf_lomb_log = models.FloatField(null=True)
  hf_lomb_log = models.FloatField(null=True)
  ttlpwr_lomb_ms2 = models.FloatField(null=True)
  lf_hf_lomb = models.FloatField(null=True)
  power_vlf_lomb = models.FloatField(null=True)
  power_lf_lomb = models.FloatField(null=True)
  power_hf_lomb = models.FloatField(null=True)
  lf_nu_lomb = models.FloatField(null=True)
  hf_nu_lomb = models.FloatField(null=True)
  ulf_welch = models.FloatField(null=True)
  vlf_welch = models.FloatField(null=True)
  lf_welch = models.FloatField(null=True)
  hf_welch = models.FloatField(null=True)
  ttlpwr_welch = models.FloatField(null=True)
  lfhf_welch = models.FloatField(null=True)
  power_vlf_welch = models.FloatField(null=True)
  power_lf_welch = models.FloatField(null=True)
  power_hf_welch = models.FloatField(null=True)
  lf_nu_welch = models.FloatField(null=True)
  hf_nu_welch = models.FloatField(null=True)

  
  def __str__(self):
    return "HRV Frequence ID: " +str(self.id)

class HRVNonLinear(models.Model):
  collected_data = models.DateTimeField(default=timezone.now) #será uma classe futuramente, não ha necessidade
  collectdata_non_lin = models.OneToOneField(        CollectData, on_delete=models.CASCADE)
  sd1 = models.FloatField(blank=True, null=True)
  sd2 = models.FloatField(blank=True, null=True)
  sd1_sd2_ratio = models.FloatField(blank=True, null=True)
  ellipse_area = models.FloatField(blank=True, null=True)
  csi = models.FloatField(blank=True, null=True)
  cvi = models.FloatField(blank=True, null=True)
  alpha1 = models.FloatField(blank=True, null=True)
  alpha2 = models.FloatField(blank=True, null=True)
  d2_10 = models.FloatField(blank=True, null=True)
  d2_20 = models.FloatField(blank=True, null=True)
  ent_aprox_1_01 = models.FloatField(blank=True, null=True)
  ent_aprox_1_015 = models.FloatField(blank=True, null=True)
  ent_aprox_1_02 = models.FloatField(blank=True, null=True)
  ent_aprox_1_025 = models.FloatField(blank=True, null=True)
  ent_aprox_2_01 = models.FloatField(blank=True, null=True)
  ent_aprox_2_015 = models.FloatField(blank=True, null=True)
  ent_aprox_2_02 = models.FloatField(blank=True, null=True)
  ent_aprox_2_025 = models.FloatField(blank=True, null=True)
  ent_amostra_1 = models.FloatField(blank=True, null=True)
  ent_amostra_2 = models.FloatField(blank=True, null=True)
  ent_multiescala_e3 = models.FloatField(blank=True, null=True)
  ent_multiescala_e5 = models.FloatField(blank=True, null=True)
  ent_fuzzy = models.FloatField(blank=True, null=True)
  ent_shannon_1 = models.FloatField(blank=True, null=True)
  ent_shannon_2 = models.FloatField(blank=True, null=True)
  ent_spectral = models.FloatField(blank=True, null=True)
  ent_permutation_1 = models.FloatField(blank=True, null=True)
  norm_entropy = models.FloatField(blank=True, null=True)
  ent_permutation_2 = models.FloatField(blank=True, null=True)
  ent_conditional = models.FloatField(blank=True, null=True)
  ent_corrected_cond = models.FloatField(blank=True, null=True)
  ctm_r1 = models.FloatField(blank=True, null=True)
  ctm_r2 = models.FloatField(blank=True, null=True)
  ctm_r3 = models.FloatField(blank=True, null=True)
  area_sodp_rr_log = models.FloatField(blank=True, null=True)
  area_sodp_rr = models.FloatField(blank=True, null=True)
  mean_dr1 = models.FloatField(blank=True, null=True)
  mean_dr2 = models.FloatField(blank=True, null=True)
  mean_dr3 = models.FloatField(blank=True, null=True)
  mean_dr4 = models.FloatField(blank=True, null=True)
  mean_dr5 = models.FloatField(blank=True, null=True)

  
  def __str__(self):
    return "HRV Non Linear ID: " + str(self.id)
