from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator

class Patient(models.Model):
  subject_name = models.CharField(max_length=200)
  age = models.PositiveSmallIntegerField(default=0) #Values from 0 to 32767
  initials = models.CharField(max_length=10)
  gender = models.PositiveSmallIntegerField(validators=[MinValueValidator(0), MaxValueValidator(10)],default=0) #(de 0 a 10)
  weight = models.FloatField(validators=[MinValueValidator(0.0), MaxValueValidator(500.0)],default=0)
  height = models.PositiveSmallIntegerField(validators=[MinValueValidator(0), MaxValueValidator(350)],default=0)

  ### ALTERAÇÕES
  phone = models.CharField(max_length=15) #numero
  #alterado address por duas colunas (estado e cidade)
  state = models.CharField(max_length=2) #estado
  city = models.CharField(max_length=50) #cidade
  ###

  bmi = models.FloatField( validators=[MinValueValidator(0.0), MaxValueValidator(150.0)], default=None)
  bsa = models.FloatField( validators=[MinValueValidator(0.0), MaxValueValidator(10.0)], default=0.0)
  smoker = models.BooleanField(default=False)
  alcohol = models.BooleanField(default=False)
  atividade_fisica = models.PositiveSmallIntegerField(validators=[MinValueValidator(0), MaxValueValidator(10)],default=0) #perguntar
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
  collected_data = models.CharField(max_length=50) #será uma classe futuramente, não ha necessidade
  observations = models.TextField(max_length=1000)


  def __str__(self):
    return self.patient_initials