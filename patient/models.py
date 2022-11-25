from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator
from smart_selects.db_fields import ChainedForeignKey
from django.utils import timezone


#Trocar ideia, data coletada automatica ou não?

GENDER_CHOICES = (
        ( 1, 'Male'),
        ( 2, 'Female'),
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

class Patient(models.Model):
  collected_data = models.DateTimeField(default=timezone.now) 
  subject_name = models.CharField(max_length=200)
  age = models.PositiveSmallIntegerField(validators=[MinValueValidator(0), MaxValueValidator(350)],default=0) #Values from 0 to 32767
  initials = models.CharField(max_length=10) #gerar
  gender = models.PositiveSmallIntegerField(validators=[MinValueValidator(1), MaxValueValidator(2)], choices=GENDER_CHOICES) # (de 1 = Male ; 2 = Female)
  weight = models.FloatField(validators=[MinValueValidator(0.0), MaxValueValidator(500.0)],default=0)
  height = models.PositiveSmallIntegerField(validators=[MinValueValidator(0), MaxValueValidator(350)],default=0)
  ### ALTERAÇÕES
  phone = models.CharField(max_length=15) #numero
  #alterado address por duas colunas (estado e cidade)
  state = models.CharField(max_length=2, choices = STATES_CHOICES)
  city = models.CharField(max_length=100)
  bmi = models.FloatField( validators=[MinValueValidator(0.0), MaxValueValidator(150.0)], default=None)
  bsa = models.FloatField( validators=[MinValueValidator(0.0), MaxValueValidator(10.0)], default=0.0)
  smoker = models.BooleanField(default=False)
  alcohol = models.BooleanField(default=False)
  physical_activity = models.PositiveSmallIntegerField(validators=[MinValueValidator(0), MaxValueValidator(10)],default=0) #perguntar
  dm = models.BooleanField(default=False)#habilitar o type_dm
  type_dm = models.PositiveSmallIntegerField(validators=[MinValueValidator(0), MaxValueValidator(2)],default=0)
  age_dm_diagnosis = models.PositiveSmallIntegerField(validators=[MinValueValidator(0), MaxValueValidator(1000)],default=0)
  dm_duration = models.PositiveSmallIntegerField(validators=[MinValueValidator(0), MaxValueValidator(1000)],default=0)
  hipo_mes = models.SmallIntegerField(default=0)
  internacao_dm = models.BooleanField(default=False)
  sbp_repous = models.PositiveSmallIntegerField(validators=[MinValueValidator(0), MaxValueValidator(1000)],default=0)
  dbp_repous = models.PositiveSmallIntegerField(validators=[MinValueValidator(0), MaxValueValidator(1000)],default=0)
  sbp_empe = models.PositiveSmallIntegerField(validators=[MinValueValidator(0), MaxValueValidator(1000)],default=0)
  dbp_empe = models.PositiveSmallIntegerField(validators=[MinValueValidator(0), MaxValueValidator(1000)],default=0)
  sbp_change = models.SmallIntegerField(default=0)
  dbp_change = models.SmallIntegerField(default=0)
  postural_drop = models.BooleanField(default=False)
  mean_hr = models.PositiveSmallIntegerField(validators=[MinValueValidator(0), MaxValueValidator(1000)],default=0)
  rr_resting = models.FloatField( validators=[MinValueValidator(0.0), MaxValueValidator(10.0)], default=0.0)
  rr_db = models.FloatField( validators=[MinValueValidator(0.0), MaxValueValidator(10.0)], default=0.0)
  rr_valsalva = models.FloatField( validators=[MinValueValidator(0.0), MaxValueValidator(10.0)], default=0.0)
  rr_standing = models.FloatField( validators=[MinValueValidator(0.0), MaxValueValidator(10.0)], default=0.0)
  obrienc_cs = models.PositiveSmallIntegerField(validators=[MinValueValidator(0), MaxValueValidator(10)],default=0) #valore possiveis
  can_status = models.PositiveSmallIntegerField(validators=[MinValueValidator(0), MaxValueValidator(10)],default=0) #valore possiveis
  brs_status = models.CharField(max_length=50) # coluna vazia
  observations = models.TextField(max_length=1000)

  def __str__(self):
    return self.initials




class Medicines(models.Model):
  collected_data = models.DateTimeField(default=timezone.now)
  patient_medicines = models.OneToOneField(
        Patient, on_delete=models.CASCADE)
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
  
def _str_(self):
  return self.patient_medicines.initials+": " + str(self.id)

class ExamsResults(models.Model):
  collected_data = models.DateTimeField(default=timezone.now)
  patient_exams = models.ForeignKey(
        Patient, on_delete=models.CASCADE)
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
    return self.patient_exams.initials+": " + str(self.id)



class CollectData(models.Model):
  collected_data = models.DateTimeField(default=timezone.now) #será uma classe futuramente, não ha necessidade
  patient_data = models.ForeignKey(
        Patient, on_delete=models.CASCADE)
  study = models.PositiveSmallIntegerField(validators=[MinValueValidator(1), MaxValueValidator(2)], choices=STUDY_CHOICES)
  ecg = models.BooleanField(default=False)
  ppg = models.BooleanField(default=False)
  abp = models.BooleanField(default=False)
  abspathrecord_times = models.PositiveSmallIntegerField(validators=[MinValueValidator(0), MaxValueValidator(1000)],default=0)
  sampling_freq_hz = models.PositiveSmallIntegerField(validators=[MinValueValidator(0), MaxValueValidator(1000)],default=0)
  device = models.PositiveSmallIntegerField(validators=[MinValueValidator(0), MaxValueValidator(1000)],default=0)
  ecg_processing_status = models.BooleanField(default=False)
  ppg_processing_status = models.BooleanField(default=False)
  brs_processing_status = models.BooleanField(default=False)
  observations = models.TextField(max_length=1000)

  def __str__(self):
    return self.patient_data.initials+": " + str(self.id)

class Conditions(models.Model):
  collected_data = models.DateTimeField(default=timezone.now)
  patient_conditions = models.OneToOneField(
        Patient, on_delete=models.CASCADE)
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
    return self.patient_conditions.initials+": " + str(self.id)
