# Generated by Django 2.2.5 on 2023-02-03 17:13

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('patient', '0049_auto_20230203_1357'),
    ]

    operations = [
        migrations.AlterField(
            model_name='collectdata',
            name='ecg_signal',
            field=models.FileField(blank=True, null=True, upload_to='txt/', verbose_name='ECG Signal (.txt)'),
        ),
        migrations.AlterField(
            model_name='collectdata',
            name='sampling_freq_hz',
            field=models.PositiveSmallIntegerField(default=0, null=True, validators=[django.core.validators.MinValueValidator(0), django.core.validators.MaxValueValidator(1000)], verbose_name='Sampling (Freq_Hz)'),
        ),
        migrations.AlterField(
            model_name='condition',
            name='ace_arb',
            field=models.BooleanField(default=False, verbose_name='ACE/ARB Therapy'),
        ),
        migrations.AlterField(
            model_name='condition',
            name='doenca_celiaca',
            field=models.BooleanField(default=False, verbose_name='Celiac Disease'),
        ),
        migrations.AlterField(
            model_name='condition',
            name='doenca_pulmonar',
            field=models.BooleanField(default=False, verbose_name='Lung Disease'),
        ),
        migrations.AlterField(
            model_name='condition',
            name='drge',
            field=models.BooleanField(default=False, verbose_name='DRGE'),
        ),
        migrations.AlterField(
            model_name='condition',
            name='pn_signs',
            field=models.CharField(max_length=200, verbose_name='PN Signs'),
        ),
        migrations.AlterField(
            model_name='condition',
            name='pn_symptoms',
            field=models.CharField(max_length=200, verbose_name='PN Symptoms'),
        ),
        migrations.AlterField(
            model_name='examsresult',
            name='acr_alb_creat',
            field=models.PositiveSmallIntegerField(default=0, validators=[django.core.validators.MinValueValidator(0), django.core.validators.MaxValueValidator(1000)], verbose_name='ACR Alb_Creat'),
        ),
        migrations.AlterField(
            model_name='examsresult',
            name='basek',
            field=models.PositiveSmallIntegerField(default=0, validators=[django.core.validators.MinValueValidator(0), django.core.validators.MaxValueValidator(1000)], verbose_name='Baseline Potássio'),
        ),
        migrations.AlterField(
            model_name='examsresult',
            name='creatina_mg_dl',
            field=models.PositiveSmallIntegerField(default=0, validators=[django.core.validators.MinValueValidator(0), django.core.validators.MaxValueValidator(1000)], verbose_name='Creatina (Mg_dL)'),
        ),
        migrations.AlterField(
            model_name='examsresult',
            name='creatina_umol_l',
            field=models.PositiveSmallIntegerField(default=0, validators=[django.core.validators.MinValueValidator(0), django.core.validators.MaxValueValidator(1000)], verbose_name='Creatina (Umol_L)'),
        ),
        migrations.AlterField(
            model_name='examsresult',
            name='ct_mg_dl',
            field=models.PositiveSmallIntegerField(default=0, validators=[django.core.validators.MinValueValidator(0), django.core.validators.MaxValueValidator(1000)], verbose_name='Colesterol Total (Mg_dL)'),
        ),
        migrations.AlterField(
            model_name='examsresult',
            name='ct_mmol_l',
            field=models.PositiveSmallIntegerField(default=0, validators=[django.core.validators.MinValueValidator(0), django.core.validators.MaxValueValidator(1000)], verbose_name='Colesterol Total (Mmol_L)'),
        ),
        migrations.AlterField(
            model_name='examsresult',
            name='glicemia_mg_dl',
            field=models.PositiveSmallIntegerField(default=0, validators=[django.core.validators.MinValueValidator(0), django.core.validators.MaxValueValidator(1000)], verbose_name='Glicemia (Mg_dL)'),
        ),
        migrations.AlterField(
            model_name='examsresult',
            name='glicemia_mmol_l',
            field=models.PositiveSmallIntegerField(default=0, validators=[django.core.validators.MinValueValidator(0), django.core.validators.MaxValueValidator(1000)], verbose_name='Glicemia (Mmol_L)'),
        ),
        migrations.AlterField(
            model_name='examsresult',
            name='hb_g_dl',
            field=models.PositiveSmallIntegerField(default=0, validators=[django.core.validators.MinValueValidator(0), django.core.validators.MaxValueValidator(1000)], verbose_name='Hb g_dL'),
        ),
        migrations.AlterField(
            model_name='examsresult',
            name='hba1c_mmol_mol',
            field=models.PositiveSmallIntegerField(default=0, validators=[django.core.validators.MinValueValidator(0), django.core.validators.MaxValueValidator(1000)], verbose_name='HbA1c (Mmol_Mol)'),
        ),
        migrations.AlterField(
            model_name='examsresult',
            name='hba1c_percent',
            field=models.PositiveSmallIntegerField(default=0, validators=[django.core.validators.MinValueValidator(0), django.core.validators.MaxValueValidator(1000)], verbose_name='HbA1c (%)'),
        ),
        migrations.AlterField(
            model_name='examsresult',
            name='hdl_mg_dl',
            field=models.PositiveSmallIntegerField(default=0, validators=[django.core.validators.MinValueValidator(0), django.core.validators.MaxValueValidator(1000)], verbose_name='HDL (Mg_dL)'),
        ),
        migrations.AlterField(
            model_name='examsresult',
            name='ldl_mg_dl',
            field=models.PositiveSmallIntegerField(default=0, validators=[django.core.validators.MinValueValidator(0), django.core.validators.MaxValueValidator(1000)], verbose_name='LDL (Mg_dL)'),
        ),
        migrations.AlterField(
            model_name='examsresult',
            name='na',
            field=models.PositiveSmallIntegerField(default=0, validators=[django.core.validators.MinValueValidator(0), django.core.validators.MaxValueValidator(1000)], verbose_name='Sódio'),
        ),
        migrations.AlterField(
            model_name='examsresult',
            name='rpc_prot_creat',
            field=models.PositiveSmallIntegerField(default=0, validators=[django.core.validators.MinValueValidator(0), django.core.validators.MaxValueValidator(1000)], verbose_name='RPC Prot_Creat'),
        ),
        migrations.AlterField(
            model_name='examsresult',
            name='tg_mg_dl',
            field=models.PositiveSmallIntegerField(default=0, validators=[django.core.validators.MinValueValidator(0), django.core.validators.MaxValueValidator(1000)], verbose_name='Triglicerídeos (Mg_dL)'),
        ),
        migrations.AlterField(
            model_name='examsresult',
            name='tg_mmol_l',
            field=models.PositiveSmallIntegerField(default=0, validators=[django.core.validators.MinValueValidator(0), django.core.validators.MaxValueValidator(1000)], verbose_name='Triglicerídeos (Mmol_L)'),
        ),
        migrations.AlterField(
            model_name='examsresult',
            name='tsh',
            field=models.PositiveSmallIntegerField(default=0, validators=[django.core.validators.MinValueValidator(0), django.core.validators.MaxValueValidator(1000)], verbose_name='Hormônio Tireoestimulante'),
        ),
        migrations.AlterField(
            model_name='examsresult',
            name='urine_albumina_mg_24h',
            field=models.PositiveSmallIntegerField(default=0, validators=[django.core.validators.MinValueValidator(0), django.core.validators.MaxValueValidator(1000)], verbose_name='Urine Albumina (Mg_24H)'),
        ),
        migrations.AlterField(
            model_name='hrvtime',
            name='cv',
            field=models.FloatField(blank=True, null=True, verbose_name='CV'),
        ),
        migrations.AlterField(
            model_name='hrvtime',
            name='hr_change',
            field=models.FloatField(blank=True, null=True, verbose_name='Hr Change'),
        ),
        migrations.AlterField(
            model_name='hrvtime',
            name='hti',
            field=models.FloatField(blank=True, null=True, verbose_name='HTI'),
        ),
        migrations.AlterField(
            model_name='hrvtime',
            name='nn20',
            field=models.FloatField(blank=True, null=True, verbose_name='NN20'),
        ),
        migrations.AlterField(
            model_name='hrvtime',
            name='nn50',
            field=models.FloatField(blank=True, null=True, verbose_name=''),
        ),
        migrations.AlterField(
            model_name='hrvtime',
            name='nn_iqr',
            field=models.FloatField(blank=True, null=True, verbose_name='NNiqr'),
        ),
        migrations.AlterField(
            model_name='hrvtime',
            name='nn_kurt',
            field=models.FloatField(blank=True, null=True, verbose_name='NN Kurt'),
        ),
        migrations.AlterField(
            model_name='hrvtime',
            name='nn_mean',
            field=models.FloatField(blank=True, null=True, verbose_name='NN Mean'),
        ),
        migrations.AlterField(
            model_name='hrvtime',
            name='nn_median',
            field=models.FloatField(blank=True, null=True, verbose_name='NN Median'),
        ),
        migrations.AlterField(
            model_name='hrvtime',
            name='nn_mode',
            field=models.FloatField(blank=True, null=True, verbose_name='NN Mode'),
        ),
        migrations.AlterField(
            model_name='hrvtime',
            name='nn_skew',
            field=models.FloatField(blank=True, null=True, verbose_name='NN Skew'),
        ),
        migrations.AlterField(
            model_name='hrvtime',
            name='nn_variance',
            field=models.FloatField(blank=True, null=True, verbose_name='NN Variance'),
        ),
        migrations.AlterField(
            model_name='hrvtime',
            name='pnn20_pr',
            field=models.FloatField(blank=True, null=True, verbose_name='pNN20 pr'),
        ),
        migrations.AlterField(
            model_name='hrvtime',
            name='pnn50_pr',
            field=models.FloatField(blank=True, null=True, verbose_name='pNN50 pr'),
        ),
        migrations.AlterField(
            model_name='hrvtime',
            name='rmssd',
            field=models.FloatField(blank=True, null=True, verbose_name='RMSSD'),
        ),
        migrations.AlterField(
            model_name='hrvtime',
            name='sd_nn',
            field=models.FloatField(blank=True, null=True, verbose_name='SDNN'),
        ),
        migrations.AlterField(
            model_name='hrvtime',
            name='sdsd',
            field=models.FloatField(blank=True, null=True, verbose_name='NN50'),
        ),
        migrations.AlterField(
            model_name='hrvtime',
            name='si',
            field=models.FloatField(blank=True, null=True, verbose_name='SI'),
        ),
        migrations.AlterField(
            model_name='hrvtime',
            name='tinn',
            field=models.FloatField(blank=True, null=True, verbose_name='TINN'),
        ),
        migrations.AlterField(
            model_name='medicine',
            name='aas_mg',
            field=models.PositiveSmallIntegerField(default=0, validators=[django.core.validators.MinValueValidator(0), django.core.validators.MaxValueValidator(1000)], verbose_name='AAS (Mg)'),
        ),
        migrations.AlterField(
            model_name='medicine',
            name='atorvas_mg',
            field=models.PositiveSmallIntegerField(default=0, validators=[django.core.validators.MinValueValidator(0), django.core.validators.MaxValueValidator(1000)], verbose_name='Atorvas (Mg)'),
        ),
        migrations.AlterField(
            model_name='medicine',
            name='carbamazpn_mg',
            field=models.PositiveSmallIntegerField(default=0, validators=[django.core.validators.MinValueValidator(0), django.core.validators.MaxValueValidator(1000)], verbose_name='Carbamazpn (Mg)'),
        ),
        migrations.AlterField(
            model_name='medicine',
            name='enalapril_mg',
            field=models.PositiveSmallIntegerField(default=0, validators=[django.core.validators.MinValueValidator(0), django.core.validators.MaxValueValidator(1000)], verbose_name='Enalapril (Mg)'),
        ),
        migrations.AlterField(
            model_name='medicine',
            name='losartan_mg',
            field=models.PositiveSmallIntegerField(default=0, validators=[django.core.validators.MinValueValidator(0), django.core.validators.MaxValueValidator(1000)], verbose_name='Losartan (Mg)'),
        ),
        migrations.AlterField(
            model_name='medicine',
            name='lt4_mg',
            field=models.PositiveSmallIntegerField(default=0, validators=[django.core.validators.MinValueValidator(0), django.core.validators.MaxValueValidator(1000)], verbose_name='LT4 (Mg)'),
        ),
        migrations.AlterField(
            model_name='medicine',
            name='mtf_mg',
            field=models.PositiveSmallIntegerField(default=0, validators=[django.core.validators.MinValueValidator(0), django.core.validators.MaxValueValidator(1000)], verbose_name='MTF (Mg)'),
        ),
        migrations.AlterField(
            model_name='medicine',
            name='omeprazol_mg',
            field=models.PositiveSmallIntegerField(default=0, validators=[django.core.validators.MinValueValidator(0), django.core.validators.MaxValueValidator(1000)], verbose_name='Omeprazol (Mg)'),
        ),
        migrations.AlterField(
            model_name='medicine',
            name='quetiapina_mg',
            field=models.PositiveSmallIntegerField(default=0, validators=[django.core.validators.MinValueValidator(0), django.core.validators.MaxValueValidator(1000)], verbose_name='Quetiapina (Mg)'),
        ),
        migrations.AlterField(
            model_name='medicine',
            name='ranitidina_mg',
            field=models.PositiveSmallIntegerField(default=0, validators=[django.core.validators.MinValueValidator(0), django.core.validators.MaxValueValidator(1000)], verbose_name='Ranitidina (Mg)'),
        ),
        migrations.AlterField(
            model_name='medicine',
            name='rosuvas_mg',
            field=models.PositiveSmallIntegerField(default=0, validators=[django.core.validators.MinValueValidator(0), django.core.validators.MaxValueValidator(1000)], verbose_name='Rosuvas (Mg)'),
        ),
        migrations.AlterField(
            model_name='medicine',
            name='sinvas_mg',
            field=models.PositiveSmallIntegerField(default=0, validators=[django.core.validators.MinValueValidator(0), django.core.validators.MaxValueValidator(1000)], verbose_name='Sinvas (Mg)'),
        ),
        migrations.AlterField(
            model_name='medicine',
            name='venlafaxina_mg',
            field=models.PositiveSmallIntegerField(default=0, validators=[django.core.validators.MinValueValidator(0), django.core.validators.MaxValueValidator(1000)], verbose_name='Venlafaxina (Mg)'),
        ),
    ]
