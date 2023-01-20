from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator
from smart_selects.db_fields import ChainedForeignKey
from django.utils import timezone
from django.contrib import admin

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

#arrumar o tipo da DM com box

class Patient(models.Model):
  collected_data = models.DateTimeField(default=timezone.now) 
  subject_name = models.CharField(max_length=200)
  age = models.PositiveSmallIntegerField(validators=[MinValueValidator(0), MaxValueValidator(150)])
  initials = models.CharField(max_length=10) #Variavel calculada
  gender = models.PositiveSmallIntegerField(validators=[MinValueValidator(1), MaxValueValidator(2)], choices=GENDER_CHOICES) 
  weight = models.FloatField(validators=[MinValueValidator(0.0), MaxValueValidator(400.0)])
  height = models.FloatField(validators=[MinValueValidator(0), MaxValueValidator(4)])
  phone = models.CharField(max_length=15, blank=True)
  state = models.CharField(max_length=2, choices = STATES_CHOICES, blank=True)
  city = models.CharField(max_length=100, blank=True)
  bmi = models.FloatField( validators=[MinValueValidator(0.0), MaxValueValidator(450.0)], default=0.0) #Variavel calculada 
  bsa = models.FloatField( validators=[MinValueValidator(0.0), MaxValueValidator(150.0)], default=0.0) #Variavel calculada
  smoker = models.BooleanField(default=False)
  alcohol = models.BooleanField(default=False)
  physical_activity = models.PositiveSmallIntegerField(validators=[MinValueValidator(0), MaxValueValidator(10)],default=0) 
  dm = models.BooleanField(default=False)# habilitar a partir da relação Dm
  type_dm = models.PositiveSmallIntegerField(validators=[MinValueValidator(0), MaxValueValidator(2)],default=0)# habilitar a partir da relação Dm
  age_dm_diagnosis = models.PositiveSmallIntegerField(validators=[MinValueValidator(0), MaxValueValidator(1000)],default=0)# habilitar a partir da relação Dm
  dm_duration = models.PositiveSmallIntegerField(validators=[MinValueValidator(0), MaxValueValidator(1000)],default=0)# habilitar a partir da relação Dm
  hipo_mes = models.SmallIntegerField(default=0)# habilitar a partir da relação Dm
  internacao_dm = models.BooleanField(default=False)# habilitar a partir da relação Dm
  sbp_repous = models.PositiveSmallIntegerField(validators=[MinValueValidator(0), MaxValueValidator(1000)], blank=True)
  dbp_repous = models.PositiveSmallIntegerField(validators=[MinValueValidator(0), MaxValueValidator(1000)], blank=True)
  sbp_empe = models.PositiveSmallIntegerField(validators=[MinValueValidator(0), MaxValueValidator(1000)], blank=True)
  dbp_empe = models.PositiveSmallIntegerField(validators=[MinValueValidator(0), MaxValueValidator(1000)], blank=True)
  sbp_change = models.SmallIntegerField(blank=True) #Variavel calculada
  dbp_change = models.SmallIntegerField(blank=True) #Variavel calculada
  postural_drop = models.BooleanField(default=False) #Variavel calculada
  mean_hr = models.PositiveSmallIntegerField(validators=[MinValueValidator(0), MaxValueValidator(1000)], blank=True)
  rr_resting = models.FloatField( validators=[MinValueValidator(0.0), MaxValueValidator(10.0)], blank=True)
  rr_db = models.FloatField( validators=[MinValueValidator(0.0), MaxValueValidator(10.0)], blank=True)
  rr_valsalva = models.FloatField( validators=[MinValueValidator(0.0), MaxValueValidator(10.0)], blank=True)
  rr_standing = models.FloatField( validators=[MinValueValidator(0.0), MaxValueValidator(10.0)], blank=True)
  obrienc_cs = models.PositiveSmallIntegerField(validators=[MinValueValidator(0), MaxValueValidator(10)], blank=True)
  can_status = models.PositiveSmallIntegerField(validators=[MinValueValidator(0), MaxValueValidator(10)], blank=True)
  brs_status = models.CharField(max_length=50,  blank=True)
  observations = models.TextField(max_length=1000,  blank=True)

  @property
  def cal_bmi(self):
    self.bmi = (self.weight / (self.height * self.height) )   


  def __str__(self):
    #return "[Paciente Iniciais: " + self.initials + " | "  + "Paciente ID: " + str(self.id)+ "]"
    return "Paciente: " + str(self.id)
#
class Medicine(models.Model):
  collected_data = models.DateTimeField(default=timezone.now)
  patient_medicines = models.ForeignKey(Patient, on_delete=models.CASCADE)
  insulin = models.BooleanField(default=False)
  ace_arb = models.BooleanField(default=False)
  sinvas_mg = models.PositiveSmallIntegerField(validators=[MinValueValidator(0), MaxValueValidator(1000)],default=0)
  atorvas_mg = models.PositiveSmallIntegerField(validators=[MinValueValidator(0), MaxValueValidator(1000)],default=0)
  rosuvas_mg = models.PositiveSmallIntegerField(validators=[MinValueValidator(0), MaxValueValidator(1000)],default=0)
  losartan_mg = models.PositiveSmallIntegerField(validators=[MinValueValidator(0), MaxValueValidator(1000)],default=0)
  enalapril_mg = models.PositiveSmallIntegerField(validators=[MinValueValidator(0), MaxValueValidator(1000)],default=0)
  quetiapina_mg = models.PositiveSmallIntegerField(validators=[MinValueValidator(0), MaxValueValidator(1000)],default=0)
  venlafaxina_mg = models.PositiveSmallIntegerField(validators=[MinValueValidator(0), MaxValueValidator(1000)],default=0)
  omeprazol_mg = models.PositiveSmallIntegerField(validators=[MinValueValidator(0), MaxValueValidator(1000)],default=0)
  ranitidina_mg = models.PositiveSmallIntegerField(validators=[MinValueValidator(0), MaxValueValidator(1000)],default=0)
  carbamazpn_mg = models.PositiveSmallIntegerField(validators=[MinValueValidator(0), MaxValueValidator(1000)],default=0)
  anticoncepcional = models.BooleanField(default=False)
  ass_mg = models.PositiveSmallIntegerField(validators=[MinValueValidator(0), MaxValueValidator(1000)],default=0)
  lt4_mg = models.PositiveSmallIntegerField(validators=[MinValueValidator(0), MaxValueValidator(1000)],default=0)
  mtf_mg = models.PositiveSmallIntegerField(validators=[MinValueValidator(0), MaxValueValidator(1000)],default=0)
  
  def __str__(self):
    #return "[Paciente ID: " + str(self.patient_medicines.id) + " | "  + "Medicamento ID: " +  str(self.id)+ "]"
    return "Medicamento: " + str(self.id)

class ExamsResult(models.Model):
  collected_data = models.DateTimeField(default=timezone.now)
  patient_exams = models.ForeignKey(Patient, on_delete=models.CASCADE)
  hba1c_percent = models.PositiveSmallIntegerField(validators=[MinValueValidator(0), MaxValueValidator(1000)],default=0)
  hba1c_mmol_mol = models.PositiveSmallIntegerField(validators=[MinValueValidator(0), MaxValueValidator(1000)],default=0) #calculado
  hb_g_dl = models.PositiveSmallIntegerField(validators=[MinValueValidator(0), MaxValueValidator(1000)],default=0)
  glicemia_mg_dl = models.PositiveSmallIntegerField(validators=[MinValueValidator(0), MaxValueValidator(1000)],default=0)
  glicemia_mmol_l = models.PositiveSmallIntegerField(validators=[MinValueValidator(0), MaxValueValidator(1000)],default=0)
  urine_albumina_mg_24h = models.PositiveSmallIntegerField(validators=[MinValueValidator(0), MaxValueValidator(1000)],default=0)
  microAlb = models.BooleanField(default=False)
  creatina_mg_dl = models.PositiveSmallIntegerField(validators=[MinValueValidator(0), MaxValueValidator(1000)],default=0)
  creatina_umol_l = models.PositiveSmallIntegerField(validators=[MinValueValidator(0), MaxValueValidator(1000)],default=0)
  acr_alb_creat = models.PositiveSmallIntegerField(validators=[MinValueValidator(0), MaxValueValidator(1000)],default=0)
  rpc_prot_creat = models.PositiveSmallIntegerField(validators=[MinValueValidator(0), MaxValueValidator(1000)],default=0)
  clear_creatinina = models.PositiveSmallIntegerField(validators=[MinValueValidator(0), MaxValueValidator(1000)],default=0)
  ct_mg_dl = models.PositiveSmallIntegerField(validators=[MinValueValidator(0), MaxValueValidator(1000)],default=0)
  ct_mmol_l = models.PositiveSmallIntegerField(validators=[MinValueValidator(0), MaxValueValidator(1000)],default=0)
  hdl_mg_dl = models.PositiveSmallIntegerField(validators=[MinValueValidator(0), MaxValueValidator(1000)],default=0)
  ldl_mg_dl = models.PositiveSmallIntegerField(validators=[MinValueValidator(0), MaxValueValidator(1000)],default=0)
  vitb12 = models.PositiveSmallIntegerField(validators=[MinValueValidator(0), MaxValueValidator(1000)],default=0)
  vitd = models.PositiveSmallIntegerField(validators=[MinValueValidator(0), MaxValueValidator(1000)],default=0)
  tsh = models.PositiveSmallIntegerField(validators=[MinValueValidator(0), MaxValueValidator(1000)],default=0)
  tg_mg_dl = models.PositiveSmallIntegerField(validators=[MinValueValidator(0), MaxValueValidator(1000)],default=0)
  tg_mmol_l = models.PositiveSmallIntegerField(validators=[MinValueValidator(0), MaxValueValidator(1000)],default=0)
  na = models.PositiveSmallIntegerField(validators=[MinValueValidator(0), MaxValueValidator(1000)],default=0)
  basek = models.PositiveSmallIntegerField(validators=[MinValueValidator(0), MaxValueValidator(1000)],default=0)
  ureia = models.PositiveSmallIntegerField(validators=[MinValueValidator(0), MaxValueValidator(1000)],default=0)

  def __str__(self):
    #return "[Paciente ID: " + str(self.patient_exams.id) + " | "  + "Resultado Exame ID: " +str(self.id)+ "]"
    return "Resultado de Exame: " +str(self.id)

class CollectData(models.Model):
  collected_data = models.DateTimeField(default=timezone.now) #será uma classe futuramente, não ha necessidade
  patient_data = models.ForeignKey(Patient, on_delete=models.CASCADE)
  study = models.PositiveSmallIntegerField(validators=[MinValueValidator(1), MaxValueValidator(10)], choices=STUDY_CHOICES)
  ecg = models.BooleanField(default=False)
  ppg = models.BooleanField(default=False)
  abp = models.BooleanField(default=False)
  emg = models.BooleanField(default=False) #NOVO CAMPO
  abspathrecord_times = models.PositiveSmallIntegerField(validators=[MinValueValidator(0), MaxValueValidator(1000)],default=0)
  sampling_freq_hz = models.PositiveSmallIntegerField(validators=[MinValueValidator(0), MaxValueValidator(1000)],default=0)
  device = models.PositiveSmallIntegerField(validators=[MinValueValidator(0), MaxValueValidator(1000)],default=0)
  file_hrv = models.FileField(null=True) # limita apenas TXT

  observations = models.TextField(max_length=1000)

  def __str__(self):
    #return "[Paciente ID: " + str(self.patient_data.id) + " | "  + "Dados Coletado ID: " + str(self.id)+ "]"
    return "Dados coletado: " + str(self.id)
#
class Condition(models.Model):
  collected_data = models.DateTimeField(default=timezone.now)
  patient_conditions = models.OneToOneField(        Patient, on_delete=models.CASCADE)
  drge = models.BooleanField(default=False)
  vitiligo = models.BooleanField(default=False)
  doenca_celiaca = models.BooleanField(default=False)
  doenca_pulmonar = models.BooleanField(default=False)
  ace_arb = models.BooleanField(default=False)
  tireoide = models.BooleanField(default=False)
  retinopathy = models.BooleanField(default=False)
  nephropathy = models.BooleanField(default=False)
  peripheral_neuropathy = models.BooleanField(default=False)
  pn_symptoms = models.CharField(max_length=200)
  pn_signs = models.CharField(max_length=200)

  def __str__(self):
    #return "[Paciente ID: " + str(self.patient_conditions.id) + " | "  + "Condições ID: " + str(self.id)+ "]"
    return "Condições: " + str(self.id)

class HRVTime(models.Model):
  collected_data = models.DateTimeField(default=timezone.now) #será uma classe futuramente, não ha necessidade
  collectdata_time = models.OneToOneField(        CollectData, on_delete=models.CASCADE)
  nn_mean = models.FloatField(null=True)
  nn_median = models.FloatField(null=True)
  nn_mode = models.FloatField(null=True)
  nn_variance = models.FloatField(null=True)
  nn_skew = models.FloatField(null=True)
  nn_kurt = models.FloatField(null=True)
  nn_iqr = models.FloatField(null=True)
  sd_nn = models.FloatField(null=True)
  cv = models.FloatField(null=True)
  rmssd = models.FloatField(null=True)
  sdsd = models.FloatField(null=True)
  nn50 = models.FloatField(null=True)
  pnn50_pr = models.FloatField(null=True)
  nn20 = models.FloatField(null=True)
  pnn20 = models.FloatField(null=True)
  pnn20_pr = models.FloatField(null=True)
  hr_change = models.FloatField(null=True)
  gti = models.FloatField(null=True)
  tinn = models.FloatField(null=True)
  si = models.FloatField(null=True)


  def __str__(self):
    #return "[Paciente ID: " + str(self.collectdata_time.patient_data.id) + " | " + "Dados Coletado ID: " + str(self.collectdata_time.id) + " | " + "HRV Time ID: " + str(self.id)+ "]"
    return str(self.collectdata_time.patient_data)

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
    return str(self.collectdata_freq.patient_data)

class HRVNonLinear(models.Model):
  collected_data = models.DateTimeField(default=timezone.now) #será uma classe futuramente, não ha necessidade
  collectdata_non_lin = models.OneToOneField(        CollectData, on_delete=models.CASCADE)
  sd1 = models.FloatField(blank=True)
  sd2 = models.FloatField(blank=True)
  sd1_sd2_ratio = models.FloatField(blank=True)
  ellipse_area = models.FloatField(blank=True)
  csi = models.FloatField(blank=True)
  cvi = models.FloatField(blank=True)
  alpha1 = models.FloatField(blank=True)
  alpha2 = models.FloatField(blank=True)
  d2_10 = models.FloatField(blank=True)
  d2_20 = models.FloatField(blank=True)
  ent_aprox_1_01 = models.FloatField(blank=True)
  ent_aprox_1_015 = models.FloatField(blank=True)
  ent_aprox_1_02 = models.FloatField(blank=True)
  ent_aprox_1_025 = models.FloatField(blank=True)
  ent_aprox_2_01 = models.FloatField(blank=True)
  ent_aprox_2_015 = models.FloatField(blank=True)
  ent_aprox_2_02 = models.FloatField(blank=True)
  ent_aprox_2_025 = models.FloatField(blank=True)
  ent_amostra_1 = models.FloatField(blank=True)
  ent_amostra_2 = models.FloatField(blank=True)
  ent_multiescala_e3 = models.FloatField(blank=True)
  ent_multiescala_e5 = models.FloatField(blank=True)
  ent_fuzzy = models.FloatField(blank=True)
  ent_shannon_1 = models.FloatField(blank=True)
  ent_shannon_2 = models.FloatField(blank=True)
  ent_spectral = models.FloatField(blank=True)
  ent_permutation_1 = models.FloatField(blank=True)
  norm_entropy = models.FloatField(blank=True)
  ent_permutation_2 = models.FloatField(blank=True)
  ent_conditional = models.FloatField(blank=True)
  ent_corrected_cond = models.FloatField(blank=True)
  ctm_r1 = models.FloatField(blank=True)
  ctm_r2 = models.FloatField(blank=True)
  ctm_r3 = models.FloatField(blank=True)
  area_sodp_rr_log = models.FloatField(blank=True)
  area_sodp_rr = models.FloatField(blank=True)
  mean_dr1 = models.FloatField(blank=True)
  mean_dr2 = models.FloatField(blank=True)
  mean_dr3 = models.FloatField(blank=True)
  mean_dr4 = models.FloatField(blank=True)
  mean_dr5 = models.FloatField(blank=True)

  
  def __str__(self):
    return str(self.collectdata_non_lin.patient_data)
