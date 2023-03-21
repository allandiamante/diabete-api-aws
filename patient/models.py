from django.db import models
from django.db.models import Min, Max, Avg
from django import forms
from django.core.validators import MaxValueValidator, MinValueValidator
from smart_selects.db_fields import ChainedForeignKey
from django.utils import timezone
from django.contrib import admin
from django.urls import reverse
from drf_spectacular.utils import extend_schema, extend_schema_view


#criar uma choice box dynamic para study_choices tabela CollectData ATENÇÃO
#criar uma choice box dynamic para device_choices tabela CollectData ATENÇÃO

GENDER_CHOICES = (
        ( 1, 'Male'),
        ( 2, 'Female'),
    )

DM_CHOICES = (
        ( 0, 'Does Not Have'),
        ( 1, 'Type 1'),
        ( 2, 'Type 2'),
        ( 3, 'Type 3 Gestational'),
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
  ("TO" , "Tocantins"))


class Patient(models.Model):
  collected_data = models.DateTimeField(verbose_name="Collected Data", default=timezone.now) 
  subject_name = models.CharField(verbose_name="Subject Name", max_length=200)
  age = models.PositiveSmallIntegerField(verbose_name="Age", validators=[MinValueValidator(0), MaxValueValidator(150)])
  initials = models.CharField(verbose_name="Initials", max_length=10) #Variavel calculada
  gender = models.PositiveSmallIntegerField(verbose_name="Gender", validators=[MinValueValidator(1), MaxValueValidator(2)], choices=GENDER_CHOICES) 
  weight = models.FloatField(verbose_name="Weight (kg)", help_text = "EX: 65,5", validators=[MinValueValidator(0.0), MaxValueValidator(400.0)])
  height = models.FloatField(verbose_name="Height (m)",  help_text = "EX: 1,82", validators=[MinValueValidator(0), MaxValueValidator(4)])
  phone = models.CharField(verbose_name="Phone", max_length=15, blank=True )
  state = models.CharField(verbose_name="State", max_length=2, choices = STATES_CHOICES, blank=True)
  city = models.CharField(verbose_name="City", max_length=100, blank=True)
  bmi = models.FloatField(verbose_name="BMI",  validators=[MinValueValidator(0.0), MaxValueValidator(450.0)], default=0.0) #Variavel calculada 
  bsa = models.FloatField(verbose_name="BSA",  validators=[MinValueValidator(0.0), MaxValueValidator(150.0)], default=0.0) #Variavel calculada
  smoker = models.BooleanField(verbose_name="Smoker", default=False)
  alcohol = models.BooleanField(verbose_name="Alcohol", default=False)
  physical_activity = models.PositiveSmallIntegerField(verbose_name="Physical Activity", validators=[MinValueValidator(0), MaxValueValidator(10)], blank=True, default=0) 
  dm = models.BooleanField(verbose_name="DM", default=False)# habilitar a partir da relação Dm
  type_dm = models.PositiveSmallIntegerField(verbose_name="Type DM", validators=[MinValueValidator(0), MaxValueValidator(3)], choices=DM_CHOICES,default=0)# habilitar a partir da relação Dm
  age_dm_diagnosis = models.PositiveSmallIntegerField(verbose_name="Age DM Diagnosis", validators=[MinValueValidator(0), MaxValueValidator(1000)],default=0)# habilitar a partir da relação Dm
  dm_duration = models.PositiveSmallIntegerField(verbose_name="DM Duration", validators=[MinValueValidator(0), MaxValueValidator(1000)],default=0)# habilitar a partir da relação Dm
  hipo_mes = models.SmallIntegerField(verbose_name="Hipo Mes", default=0)# habilitar a partir da relação Dm
  internacao_dm = models.BooleanField(verbose_name="Internation DM", default=False)# habilitar a partir da relação Dm
  sbp_repous = models.PositiveSmallIntegerField(verbose_name="SDP Repous", validators=[MinValueValidator(0), MaxValueValidator(1000)], blank=True, null=True)
  dbp_repous = models.PositiveSmallIntegerField(verbose_name="DBP Repous", validators=[MinValueValidator(0), MaxValueValidator(1000)], blank=True, null=True)
  sbp_empe = models.PositiveSmallIntegerField(verbose_name="SDP Empe", validators=[MinValueValidator(0), MaxValueValidator(1000)], blank=True, null=True)
  dbp_empe = models.PositiveSmallIntegerField(verbose_name="DBP Empe", validators=[MinValueValidator(0), MaxValueValidator(1000)], blank=True, null=True)
  sbp_change = models.SmallIntegerField(verbose_name="SDP Change", blank=True, null=True) #Variavel calculada
  dbp_change = models.SmallIntegerField(verbose_name="DBP Change", blank=True, null=True) #Variavel calculada
  postural_drop = models.BooleanField(verbose_name="Postural Drop", blank=True, null=True) #Variavel calculada
  mean_hr = models.PositiveSmallIntegerField(verbose_name="Mean Hr", validators=[MinValueValidator(0), MaxValueValidator(1000)], blank=True, null=True)
  rr_resting = models.FloatField(verbose_name="RR Resting",  validators=[MinValueValidator(0.0), MaxValueValidator(10.0)], blank=True, null=True)
  rr_db = models.FloatField(verbose_name="RR Deep Breathing",  validators=[MinValueValidator(0.0), MaxValueValidator(10.0)], blank=True, null=True)
  rr_valsalva = models.FloatField(verbose_name="RR Valsalva",  validators=[MinValueValidator(0.0), MaxValueValidator(10.0)], blank=True, null=True)
  rr_standing = models.FloatField(verbose_name="RR Standing",  validators=[MinValueValidator(0.0), MaxValueValidator(10.0)], blank=True, null=True)
  obrienc_cs = models.PositiveSmallIntegerField(verbose_name="Obrienc CS", validators=[MinValueValidator(0), MaxValueValidator(10)], blank=True, null=True)
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
  patient_medicines = models.ForeignKey( Patient, on_delete=models.CASCADE, verbose_name="Patient ID")
  insulin = models.BooleanField(verbose_name="Insulin", default=False)
  ace_arb = models.BooleanField(verbose_name="Ace Arb", default=False)
  sinvas_mg = models.PositiveSmallIntegerField(verbose_name="Sinvas (Mg)", validators=[MinValueValidator(0), MaxValueValidator(1000)], blank=True, null=True)
  atorvas_mg = models.PositiveSmallIntegerField(verbose_name="Atorvas (Mg)", validators=[MinValueValidator(0), MaxValueValidator(1000)], blank=True, null=True)
  rosuvas_mg = models.PositiveSmallIntegerField(verbose_name="Rosuvas (Mg)", validators=[MinValueValidator(0), MaxValueValidator(1000)], blank=True, null=True)
  losartan_mg = models.PositiveSmallIntegerField(verbose_name="Losartan (Mg)", validators=[MinValueValidator(0), MaxValueValidator(1000)], blank=True, null=True)
  enalapril_mg = models.PositiveSmallIntegerField(verbose_name="Enalapril (Mg)", validators=[MinValueValidator(0), MaxValueValidator(1000)], blank=True, null=True)
  quetiapina_mg = models.PositiveSmallIntegerField(verbose_name="Quetiapina (Mg)", validators=[MinValueValidator(0), MaxValueValidator(1000)], blank=True, null=True)
  venlafaxina_mg = models.PositiveSmallIntegerField(verbose_name="Venlafaxina (Mg)", validators=[MinValueValidator(0), MaxValueValidator(1000)], blank=True, null=True)
  omeprazol_mg = models.PositiveSmallIntegerField(verbose_name="Omeprazol (Mg)", validators=[MinValueValidator(0), MaxValueValidator(1000)], blank=True, null=True)
  ranitidina_mg = models.PositiveSmallIntegerField(verbose_name="Ranitidina (Mg)", validators=[MinValueValidator(0), MaxValueValidator(1000)], blank=True, null=True)
  carbamazpn_mg = models.PositiveSmallIntegerField(verbose_name="Carbamazpn (Mg)", validators=[MinValueValidator(0), MaxValueValidator(1000)], blank=True, null=True)
  anticoncepcional = models.BooleanField(verbose_name="Anticoncepcional",default=False)
  aas_mg = models.PositiveSmallIntegerField(verbose_name="AAS (Mg)", validators=[MinValueValidator(0), MaxValueValidator(1000)], blank=True, null=True)
  lt4_mg = models.PositiveSmallIntegerField(verbose_name="LT4 (Mg)", validators=[MinValueValidator(0), MaxValueValidator(1000)], blank=True, null=True)
  mtf_mg = models.PositiveSmallIntegerField(verbose_name="MTF (Mg)", validators=[MinValueValidator(0), MaxValueValidator(1000)], blank=True, null=True)
  observations = models.TextField(verbose_name="Observations", max_length=1000,  blank=True, null=True)
  
  def __str__(self):
    #return "[Paciente ID: " + str(self.patient_medicines.id) + " | "  + "Medicamento ID: " +  str(self.id)+ "]"
    return "Medicine ID: " + str(self.id)

  def get_absolute_url(self):
    return reverse('medicine')  

class ExamsResult(models.Model):
  collected_data = models.DateTimeField(verbose_name="Collected Data",default=timezone.now)
  patient_exams = models.ForeignKey(Patient,verbose_name="Patient ID", on_delete=models.CASCADE)
  hba1c_percent = models.PositiveSmallIntegerField(verbose_name="HbA1c (%)", validators=[MinValueValidator(0), MaxValueValidator(1000)], null=True)
  hba1c_mmol_mol = models.PositiveSmallIntegerField(verbose_name="HbA1c (Mmol_Mol)", validators=[MinValueValidator(0), MaxValueValidator(1000)], blank=True, null=True) #calculado
  hb_g_dl = models.PositiveSmallIntegerField(verbose_name="Hb (g_dL)", validators=[MinValueValidator(0), MaxValueValidator(1000)], blank=True, null=True)
  glicemia_mg_dl = models.PositiveSmallIntegerField(verbose_name="Glicemia (Mg_dL)", validators=[MinValueValidator(0), MaxValueValidator(1000)], blank=True, null=True)
  glicemia_mmol_l = models.PositiveSmallIntegerField(verbose_name="Glicemia (Mmol_L)", validators=[MinValueValidator(0), MaxValueValidator(1000)], blank=True, null=True)
  urine_albumina_mg_24h = models.PositiveSmallIntegerField(verbose_name="Urine Albumina (Mg_24H)", validators=[MinValueValidator(0), MaxValueValidator(1000)], blank=True, null=True)
  microAlb = models.BooleanField(verbose_name="Micro Alb", default=False)
  creatina_mg_dl = models.PositiveSmallIntegerField(verbose_name="Creatina (Mg_dL)", validators=[MinValueValidator(0), MaxValueValidator(1000)], blank=True, null=True)
  creatina_umol_l = models.PositiveSmallIntegerField(verbose_name="Creatina (Umol_L)", validators=[MinValueValidator(0), MaxValueValidator(1000)], blank=True, null=True)
  acr_alb_creat = models.PositiveSmallIntegerField(verbose_name="ACR Alb_Creat", validators=[MinValueValidator(0), MaxValueValidator(1000)], blank=True, null=True)
  rpc_prot_creat = models.PositiveSmallIntegerField(verbose_name="RPC Prot_Creat", validators=[MinValueValidator(0), MaxValueValidator(1000)], blank=True, null=True)
  clear_creatinina = models.PositiveSmallIntegerField(verbose_name="Clear Creatinina", validators=[MinValueValidator(0), MaxValueValidator(1000)], blank=True, null=True)
  ct_mg_dl = models.PositiveSmallIntegerField(verbose_name="Colesterol Total (Mg_dL)", validators=[MinValueValidator(0), MaxValueValidator(1000)], blank=True, null=True)
  ct_mmol_l = models.PositiveSmallIntegerField(verbose_name="Colesterol Total (Mmol_L)", validators=[MinValueValidator(0), MaxValueValidator(1000)], blank=True, null=True)
  hdl_mg_dl = models.PositiveSmallIntegerField(verbose_name="HDL (Mg_dL)", validators=[MinValueValidator(0), MaxValueValidator(1000)], blank=True, null=True)
  ldl_mg_dl = models.PositiveSmallIntegerField(verbose_name="LDL (Mg_dL)", validators=[MinValueValidator(0), MaxValueValidator(1000)], blank=True, null=True)
  vitb12 = models.PositiveSmallIntegerField(verbose_name="Vit B12", validators=[MinValueValidator(0), MaxValueValidator(1000)], blank=True, null=True)
  vitd = models.PositiveSmallIntegerField(verbose_name="Vit D", validators=[MinValueValidator(0), MaxValueValidator(1000)], blank=True, null=True)
  tsh = models.PositiveSmallIntegerField(verbose_name="Hormônio Tireoestimulante", validators=[MinValueValidator(0), MaxValueValidator(1000)], blank=True, null=True)
  tg_mg_dl = models.PositiveSmallIntegerField(verbose_name="Triglicerídeos (Mg_dL)", validators=[MinValueValidator(0), MaxValueValidator(1000)], blank=True, null=True)
  tg_mmol_l = models.PositiveSmallIntegerField(verbose_name="Triglicerídeos (Mmol_L)", validators=[MinValueValidator(0), MaxValueValidator(1000)], blank=True, null=True)
  na = models.PositiveSmallIntegerField(verbose_name="Sódio", validators=[MinValueValidator(0), MaxValueValidator(1000)], blank=True, null=True)
  basek = models.PositiveSmallIntegerField(verbose_name="Baseline Potássio", validators=[MinValueValidator(0), MaxValueValidator(1000)], blank=True, null=True)
  ureia = models.PositiveSmallIntegerField(verbose_name="Ureia", validators=[MinValueValidator(0), MaxValueValidator(1000)], blank=True, null=True)

  def __str__(self):
    #return "[Paciente ID: " + str(self.patient_exams.id) + " | "  + "Resultado Exame ID: " +str(self.id)+ "]"
    return "Exams Result ID: " +str(self.id)

class Condition(models.Model):
  collected_data = models.DateTimeField(verbose_name="Collected Data", default=timezone.now)
  patient_conditions = models.OneToOneField(Patient, verbose_name="Patient ID",on_delete=models.CASCADE)
  drge = models.BooleanField(verbose_name="DRGE", default=False)
  vitiligo = models.BooleanField(verbose_name="Vitiligo", default=False)
  doenca_celiaca = models.BooleanField(verbose_name="Celiac Disease", default=False)
  doenca_pulmonar = models.BooleanField(verbose_name="Lung Disease", default=False)
  ace_arb = models.BooleanField(verbose_name="ACE/ARB Therapy", default=False)
  tireoide = models.BooleanField(verbose_name="Tireoide", default=False)
  retinopathy = models.BooleanField(verbose_name="Retinopathy", default=False)
  nephropathy = models.BooleanField(verbose_name="Nephropathy", default=False)
  peripheral_neuropathy = models.BooleanField(verbose_name="Peripheral Neuropathy", default=False)
  pn_symptoms = models.CharField(verbose_name="PN Symptoms", max_length=200,  blank=True, null=True )
  pn_signs = models.CharField(verbose_name="PN Signs", max_length=200,  blank=True, null=True)

  def __str__(self):
    #return "[Paciente ID: " + str(self.patient_conditions.id) + " | "  + "Condições ID: " + str(self.id)+ "]"
    return "Condition ID: " + str(self.id)

class Study(models.Model):
  collected_data = models.DateTimeField(verbose_name="Collected Data", default=timezone.now) #será uma classe futuramente, não ha necessidade
  name_study = models.CharField(verbose_name="Study Name", max_length=200 )

  def __str__(self):
    return self.name_study

class CollectData(models.Model):
  collected_data = models.DateTimeField(verbose_name="Collected Data", default=timezone.now) #será uma classe futuramente, não ha necessidade
  patient_data = models.ForeignKey(Patient, verbose_name="Patient ID",  on_delete=models.CASCADE)
  study = models.ForeignKey(Study, verbose_name="Study",  on_delete=models.CASCADE)
  ecg = models.BooleanField(verbose_name="ECG", default=False,  blank=True, null=True)
  ppg = models.BooleanField(verbose_name="PPG", default=False,  blank=True, null=True)
  abp = models.BooleanField(verbose_name="ABP", default=False,  blank=True, null=True)
  emg = models.BooleanField(verbose_name="EMG", default=False,  blank=True, null=True) #NOVO CAMPO
  abspathrecord_times = models.PositiveSmallIntegerField(verbose_name="Abspathrecord Times", validators=[MinValueValidator(0), MaxValueValidator(1000)],default=0,  blank=True, null=True)
  sampling_freq_hz = models.PositiveSmallIntegerField(verbose_name="Sampling (Freq_Hz)", validators=[MinValueValidator(0), MaxValueValidator(1000)],default=0,  blank=True, null=True)
  device = models.PositiveSmallIntegerField(verbose_name="Device", validators=[MinValueValidator(0), MaxValueValidator(1000)],default=0,  blank=True, null=True)
  ecg_signal = models.FileField(verbose_name="ECG Signal (.txt)", upload_to="txt/",blank=True, null=True) # limita apenas TXT
  observations = models.TextField(verbose_name="Observations", max_length=1000, blank=True, null=True)

  def __str__(self):
    #return "[Paciente ID: " + str(self.patient_data.id) + " | "  + "Dados Coletado ID: " + str(self.id)+ "]"
    return "Collect Data ID: " + str(self.id)

class HRVTime(models.Model):
  collected_data = models.DateTimeField(verbose_name="Collected Data", default=timezone.now)
  collectdata_time = models.OneToOneField(CollectData, verbose_name="Collect Data ID",on_delete=models.CASCADE)
  nn_mean = models.FloatField(null=True, blank=True, verbose_name="NN Mean")
  nn_median = models.FloatField(null=True, blank=True, verbose_name="NN Median")
  nn_mode = models.FloatField(null=True, blank=True, verbose_name="NN Mode")
  nn_variance = models.FloatField(null=True, blank=True, verbose_name="NN Variance")
  nn_skew = models.FloatField(null=True, blank=True, verbose_name="NN Skewness")
  nn_kurt = models.FloatField(null=True, blank=True, verbose_name="NN Kurtosis")
  nn_iqr = models.FloatField(null=True, blank=True, verbose_name="NN Interquartile")
  sd_nn = models.FloatField(null=True, blank=True, verbose_name="SD NN")
  cv = models.FloatField(null=True, blank=True, verbose_name="Coefficient Variation")
  rmssd = models.FloatField(null=True, blank=True, verbose_name="RMSSD")
  sdsd = models.FloatField(null=True, blank=True, verbose_name="SDSD")
  nn50 = models.FloatField(null=True, blank=True, verbose_name="NN (50ms)")
  pnn50_pr = models.FloatField(null=True, blank=True, verbose_name="pNN (50ms) pr")
  nn20 = models.FloatField(null=True, blank=True, verbose_name="NN (20ms)")
  pnn20_pr = models.FloatField(null=True, blank=True, verbose_name="pNN (20ms) pr ")
  hr_change = models.FloatField(null=True, blank=True, verbose_name="Hr Change")
  hti = models.FloatField(null=True, blank=True, verbose_name="HTI")
  tinn = models.FloatField(null=True, blank=True, verbose_name="TINN")
  si = models.FloatField(null=True, blank=True, verbose_name="SI")

  numeric_fields = ['nn_mean','nn_median','nn_mode','nn_variance','nn_skew','nn_kurt','nn_iqr','sd_nn','cv','rmssd','sdsd','nn50','pnn50_pr','nn20','pnn20_pr','hr_change','hti','tinn','si']

  def __str__(self):
    #return "[Paciente ID: " + str(self.collectdata_time.patient_data.id) + " | " + "Dados Coletado ID: " + str(self.collectdata_time.id) + " | " + "HRV Time ID: " + str(self.id)+ "]"
    return "HRV Time ID: " + str(self.id)

  
  def normalize_data(self, data):
    # Recupera os valores mínimos e máximos de cada campo numérico
    valores_min = []
    valores_max = []
    valores_avg = []

    for field in HRVTime._meta.fields[3:]:      
      valores_min.append(HRVTime.objects.aggregate(Min(field.name)))
      valores_max.append(HRVTime.objects.aggregate(Max(field.name)))
      valores_avg.append(HRVTime.objects.aggregate(Avg(field.name)))


    novo_item = {}
    for item in data:


      for field, valor in item.items():
        novo_item[field + '_normalized'] = valor

        
        if field in HRVTime.numeric_fields:
          valor_min = valores_min[HRVTime.numeric_fields.index(field)][f"{field}__min"]
          valor_max = valores_max[HRVTime.numeric_fields.index(field)][f"{field}__max"]
          valor_avg = valores_avg[HRVTime.numeric_fields.index(field)][f"{field}__avg"]

          if( valor != None):
            if valor_max == valor_min:
              # Define o valor normalizado como 0 ou outro valor padrão.
              novo_item[field + '_normalized'] = 0
            else:
              # Normaliza o valor.
              novo_item[field + '_normalized'] = (valor - valor_min) / (valor_max - valor_min)
          else:
            if valor_max == valor_min:
                novo_item[field + '_normalized'] = 0
            else:            
                novo_item[field + '_normalized'] = (valor_avg - valor_min) / (valor_max - valor_min)
    return novo_item

class HRVFreq(models.Model):
  collected_data = models.DateTimeField(verbose_name="Collected Data", default=timezone.now) #será uma classe futuramente, não ha necessida
  collectdata_freq = models.OneToOneField(CollectData, verbose_name="Collect Data ID", on_delete=models.CASCADE)
  ulf_lomb_ms2 = models.FloatField(null=True, blank=True, verbose_name="Ultra Low Frequency Lomb (≤0.003 Hz)")
  vlf_lomb_ms2 = models.FloatField(null=True, blank=True, verbose_name="Very Low Frequency Lomb (0.0033–0.04 Hz)")
  lf_lomb_ms2 = models.FloatField(null=True, blank=True, verbose_name="Low Frequency Lomb (0.04–0.15 Hz)")
  hf_lomb_ms2 = models.FloatField(null=True, blank=True, verbose_name="High Frequency Lomb (0.15–0.4 Hz)")
  ulf_lomb_log = models.FloatField(null=True, blank=True, verbose_name="ULF Lomb Log")
  vlf_lomb_log = models.FloatField(null=True, blank=True, verbose_name="VLF Lomb Log")
  lf_lomb_log = models.FloatField(null=True, blank=True, verbose_name="LF Lomb Log")
  hf_lomb_log = models.FloatField(null=True, blank=True, verbose_name="HF Lomb Log")
  ttlpwr_lomb_ms2 = models.FloatField(null=True, blank=True, verbose_name="TTLPWR Lomb Ms2")
  lf_hf_lomb = models.FloatField(null=True, blank=True, verbose_name="LF Hf_Lomb")
  power_vlf_lomb = models.FloatField(null=True, blank=True, verbose_name="Power VLF Lomb")
  power_lf_lomb = models.FloatField(null=True, blank=True, verbose_name="Power LF Lomb")
  power_hf_lomb = models.FloatField(null=True, blank=True, verbose_name="Power HF Lomb")
  lf_nu_lomb = models.FloatField(null=True, blank=True, verbose_name="LF NU Lomb")
  hf_nu_lomb = models.FloatField(null=True, blank=True, verbose_name="HF NU Lomb")
  ulf_welch = models.FloatField(null=True, blank=True, verbose_name="ULF Welch")
  vlf_welch = models.FloatField(null=True, blank=True, verbose_name="VLF Welch")
  lf_welch = models.FloatField(null=True, blank=True, verbose_name="LF Welch")
  hf_welch = models.FloatField(null=True, blank=True, verbose_name="HF Welch")
  ttlpwr_welch = models.FloatField(null=True, blank=True, verbose_name="TTLPWR Welch")
  lfhf_welch = models.FloatField(null=True, blank=True, verbose_name="LF HF Welch")
  power_vlf_welch = models.FloatField(null=True, blank=True, verbose_name="Power VLF Welch")
  power_lf_welch = models.FloatField(null=True, blank=True, verbose_name="Power LF Welch")
  power_hf_welch = models.FloatField(null=True, blank=True, verbose_name="Power HF Welch")
  lf_nu_welch = models.FloatField(null=True, blank=True, verbose_name="LF NU Welch")
  hf_nu_welch = models.FloatField(null=True,  blank=True, verbose_name="HF NU Welch")

  numeric_fields = ['ulf_lomb_ms2', 'vlf_lomb_ms2', 'lf_lomb_ms2', 'hf_lomb_ms2', 'ulf_lomb_log', 'vlf_lomb_log', 'lf_lomb_log', 'hf_lomb_log', 'ttlpwr_lomb_ms2', 'lf_hf_lomb', 'power_vlf_lomb', 'power_lf_lomb', 'power_hf_lomb', 'lf_nu_lomb', 'hf_nu_lomb', 'ulf_welch', 'vlf_welch', 'lf_welch', 'hf_welch', 'ttlpwr_welch', 'lfhf_welch', 'power_vlf_welch', 'power_lf_welch', 'power_hf_welch', 'lf_nu_welch', 'hf_nu_welch']
  
  def __str__(self):
    return "HRV Frequency ID: " +str(self.id)

  
  def normalize_data(self, data):
    # Recupera os valores mínimos e máximos de cada campo numérico
    valores_min = []
    valores_max = []
    valores_avg = []

    for field in HRVFreq._meta.fields[3:]:      
      valores_min.append(HRVFreq.objects.aggregate(Min(field.name)))
      valores_max.append(HRVFreq.objects.aggregate(Max(field.name)))
      valores_avg.append(HRVFreq.objects.aggregate(Avg(field.name)))


    novo_item = {}
    for item in data:


      for field, valor in item.items():
        novo_item[field + '_normalized'] = valor

        
        if field in HRVFreq.numeric_fields:
          valor_min = valores_min[HRVFreq.numeric_fields.index(field)][f"{field}__min"]
          valor_max = valores_max[HRVFreq.numeric_fields.index(field)][f"{field}__max"]
          valor_avg = valores_avg[HRVFreq.numeric_fields.index(field)][f"{field}__avg"]

          if( valor != None):
            if valor_max == valor_min:
              # Define o valor normalizado como 0 ou outro valor padrão.
              novo_item[field + '_normalized'] = 0
            else:
              # Normaliza o valor.
              novo_item[field + '_normalized'] = (valor - valor_min) / (valor_max - valor_min)
          else:
            if valor_max == valor_min:
                novo_item[field + '_normalized'] = 0
            else:            
                novo_item[field + '_normalized'] = (valor_avg - valor_min) / (valor_max - valor_min)
    return novo_item

class HRVNonLinear(models.Model):
  collected_data = models.DateTimeField(default=timezone.now, verbose_name="Collected Data")
  collectdata_non_lin = models.OneToOneField(        CollectData, on_delete=models.CASCADE, verbose_name="Collect Data ID")
  sd1 = models.FloatField(blank=True, null=True, verbose_name="Standard Deviation Perpendicular")
  sd2 = models.FloatField(blank=True, null=True, verbose_name="Standard Deviation Along")
  sd1_sd2_ratio = models.FloatField(blank=True, null=True, verbose_name="SD_Perp SD_Along Ratio")
  ellipse_area = models.FloatField(blank=True, null=True, verbose_name="Ellipse Area")
  csi = models.FloatField(blank=True, null=True, verbose_name="Cardiac Sympathetic Index")
  cvi = models.FloatField(blank=True, null=True, verbose_name="Cardiac Vagal Index")
  alpha1 = models.FloatField(blank=True, null=True, verbose_name="Alpha 1")
  alpha2 = models.FloatField(blank=True, null=True, verbose_name="Alpha 2")
  d2_10 = models.FloatField(blank=True, null=True, verbose_name="D2 (dimension 10)")
  d2_20 = models.FloatField(blank=True, null=True, verbose_name="D2 (dimension 20)")
  ent_aprox_1_01 = models.FloatField(blank=True, null=True, verbose_name="Entropy Aprox_1_01")
  ent_aprox_1_015 = models.FloatField(blank=True, null=True, verbose_name="Entropy Aprox_1_015")
  ent_aprox_1_02 = models.FloatField(blank=True, null=True, verbose_name="Entropy Aprox_1_02")
  ent_aprox_1_025 = models.FloatField(blank=True, null=True, verbose_name="Entropy Aprox_1_025")
  ent_aprox_2_01 = models.FloatField(blank=True, null=True, verbose_name="Entropy Aprox_2_01")
  ent_aprox_2_015 = models.FloatField(blank=True, null=True, verbose_name="Entropy Aprox_2_015")
  ent_aprox_2_02 = models.FloatField(blank=True, null=True, verbose_name="Entropy Aprox_2_02")
  ent_aprox_2_025 = models.FloatField(blank=True, null=True, verbose_name="Entropy Aprox_2_025")
  ent_amostra_1 = models.FloatField(blank=True, null=True, verbose_name="Entropy Amostra_1")
  ent_amostra_2 = models.FloatField(blank=True, null=True, verbose_name="Entropy Amostra_2")
  ent_multiescala_e3 = models.FloatField(blank=True, null=True, verbose_name="Entropy Multiescala_E3")
  ent_multiescala_e5 = models.FloatField(blank=True, null=True, verbose_name="Entropy Multiescala_E5")
  ent_fuzzy = models.FloatField(blank=True, null=True, verbose_name="Entropy Fuzzy")
  ent_shannon_1 = models.FloatField(blank=True, null=True, verbose_name="Entropy Shannon1")
  ent_shannon_2 = models.FloatField(blank=True, null=True, verbose_name="Entropy Shannon_2")
  ent_spectral = models.FloatField(blank=True, null=True, verbose_name="Entropy Spectral")
  ent_permutation_1 = models.FloatField(blank=True, null=True, verbose_name="Entropy Permutation_1")
  norm_entropy = models.FloatField(blank=True, null=True, verbose_name="Norm Entropy")
  ent_permutation_2 = models.FloatField(blank=True, null=True, verbose_name="Entropy Permutation_2")
  ent_conditional = models.FloatField(blank=True, null=True, verbose_name="Entropy Conditional")
  ent_corrected_cond = models.FloatField(blank=True, null=True, verbose_name="Entropy Corrected_Cond")
  ctm_r1 = models.FloatField(blank=True, null=True, verbose_name="Ctm R1 (r = 10)")
  ctm_r2 = models.FloatField(blank=True, null=True, verbose_name="Ctm R2 (r = 20)")
  ctm_r3 = models.FloatField(blank=True, null=True, verbose_name="Ctm R3 (r = 40)")
  area_sodp_rr_log = models.FloatField(blank=True, null=True, verbose_name="Area Sodp RR (log)")
  area_sodp_rr = models.FloatField(blank=True, null=True, verbose_name="Area Sodp RR")
  mean_dr1 = models.FloatField(blank=True, null=True, verbose_name="Mean Dr1 (r = 10)")
  mean_dr2 = models.FloatField(blank=True, null=True, verbose_name="Mean Dr2 (r = 20)")
  mean_dr3 = models.FloatField(blank=True, null=True, verbose_name="Mean Dr3 (r = 40)")
  mean_dr4 = models.FloatField(blank=True, null=True, verbose_name="Mean Dr4 (r = 60)")
  mean_dr5 = models.FloatField(blank=True, null=True, verbose_name="Mean Dr5 (r = 80)")
  
  numeric_fields = [
  'sd1','sd2','sd1_sd2_ratio','ellipse_area','csi','cvi','alpha1','alpha2','d2_10','d2_20',
  'ent_aprox_1_01','ent_aprox_1_015','ent_aprox_1_02','ent_aprox_1_025','ent_aprox_2_01','ent_aprox_2_015','ent_aprox_2_02',
  'ent_aprox_2_025','ent_amostra_1','ent_amostra_2','ent_multiescala_e3','ent_multiescala_e5','ent_fuzzy','ent_shannon_1',
  'ent_shannon_2','ent_spectral','ent_permutation_1','norm_entropy','ent_permutation_2','ent_conditional','ent_corrected_cond',
  'ctm_r1','ctm_r2','ctm_r3','area_sodp_rr_log','area_sodp_rr','mean_dr1','mean_dr2','mean_dr3','mean_dr4','mean_dr5']
    
  def __str__(self):
    return "HRV Non Linear ID: " + str(self.id)


  def normalize_data(self, data):
    # Recupera os valores mínimos e máximos de cada campo numérico
    valores_min = []
    valores_max = []
    valores_avg = []

    for field in HRVNonLinear._meta.fields[3:]:      
      valores_min.append(HRVNonLinear.objects.aggregate(Min(field.name)))
      valores_max.append(HRVNonLinear.objects.aggregate(Max(field.name)))
      valores_avg.append(HRVNonLinear.objects.aggregate(Avg(field.name)))


    novo_item = {}
    for item in data:


      for field, valor in item.items():
        novo_item[field + '_normalized'] = valor

        
        if field in HRVNonLinear.numeric_fields:
          valor_min = valores_min[HRVNonLinear.numeric_fields.index(field)][f"{field}__min"]
          valor_max = valores_max[HRVNonLinear.numeric_fields.index(field)][f"{field}__max"]
          valor_avg = valores_avg[HRVNonLinear.numeric_fields.index(field)][f"{field}__avg"]

          if( valor != None):
            if valor_max == valor_min:
              # Define o valor normalizado como 0 ou outro valor padrão.
              novo_item[field + '_normalized'] = 0
            else:
              # Normaliza o valor.
              novo_item[field + '_normalized'] = (valor - valor_min) / (valor_max - valor_min)
          else:
            if valor_max == valor_min:
                novo_item[field + '_normalized'] = 0
            else:            
                novo_item[field + '_normalized'] = (valor_avg - valor_min) / (valor_max - valor_min)
    return novo_item

    