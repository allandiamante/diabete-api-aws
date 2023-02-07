# Generated by Django 2.2.5 on 2023-02-03 17:42

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('patient', '0050_auto_20230203_1413'),
    ]

    operations = [
        migrations.AlterField(
            model_name='hrvfreq',
            name='collectdata_freq',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='patient.CollectData', verbose_name='Collect Data Frequence'),
        ),
        migrations.AlterField(
            model_name='hrvfreq',
            name='collected_data',
            field=models.DateTimeField(default=django.utils.timezone.now, verbose_name='Collected Data'),
        ),
        migrations.AlterField(
            model_name='hrvfreq',
            name='hf_lomb_log',
            field=models.FloatField(blank=True, null=True, verbose_name='HF Lomb Log'),
        ),
        migrations.AlterField(
            model_name='hrvfreq',
            name='hf_lomb_ms2',
            field=models.FloatField(blank=True, null=True, verbose_name='High Frequency Lomb (0.15–0.4 Hz)'),
        ),
        migrations.AlterField(
            model_name='hrvfreq',
            name='hf_nu_lomb',
            field=models.FloatField(blank=True, null=True, verbose_name='HF NU Lomb'),
        ),
        migrations.AlterField(
            model_name='hrvfreq',
            name='hf_nu_welch',
            field=models.FloatField(blank=True, null=True, verbose_name='HF NU Welch'),
        ),
        migrations.AlterField(
            model_name='hrvfreq',
            name='hf_welch',
            field=models.FloatField(blank=True, null=True, verbose_name='HF Welch'),
        ),
        migrations.AlterField(
            model_name='hrvfreq',
            name='lf_hf_lomb',
            field=models.FloatField(blank=True, null=True, verbose_name='LF Hf_Lomb'),
        ),
        migrations.AlterField(
            model_name='hrvfreq',
            name='lf_lomb_log',
            field=models.FloatField(blank=True, null=True, verbose_name='LF Lomb Log'),
        ),
        migrations.AlterField(
            model_name='hrvfreq',
            name='lf_lomb_ms2',
            field=models.FloatField(blank=True, null=True, verbose_name='Low Frequency Lomb (0.04–0.15 Hz)'),
        ),
        migrations.AlterField(
            model_name='hrvfreq',
            name='lf_nu_lomb',
            field=models.FloatField(blank=True, null=True, verbose_name='LF NU Lomb'),
        ),
        migrations.AlterField(
            model_name='hrvfreq',
            name='lf_nu_welch',
            field=models.FloatField(blank=True, null=True, verbose_name='LF NU Welch'),
        ),
        migrations.AlterField(
            model_name='hrvfreq',
            name='lf_welch',
            field=models.FloatField(blank=True, null=True, verbose_name='LF Welch'),
        ),
        migrations.AlterField(
            model_name='hrvfreq',
            name='lfhf_welch',
            field=models.FloatField(blank=True, null=True, verbose_name='LF HF Welch'),
        ),
        migrations.AlterField(
            model_name='hrvfreq',
            name='power_hf_lomb',
            field=models.FloatField(blank=True, null=True, verbose_name='Power HF Lomb'),
        ),
        migrations.AlterField(
            model_name='hrvfreq',
            name='power_hf_welch',
            field=models.FloatField(blank=True, null=True, verbose_name='Power HF Welch'),
        ),
        migrations.AlterField(
            model_name='hrvfreq',
            name='power_lf_lomb',
            field=models.FloatField(blank=True, null=True, verbose_name='Power LF Lomb'),
        ),
        migrations.AlterField(
            model_name='hrvfreq',
            name='power_lf_welch',
            field=models.FloatField(blank=True, null=True, verbose_name='Power LF Welch'),
        ),
        migrations.AlterField(
            model_name='hrvfreq',
            name='power_vlf_lomb',
            field=models.FloatField(blank=True, null=True, verbose_name='Power VLF Lomb'),
        ),
        migrations.AlterField(
            model_name='hrvfreq',
            name='power_vlf_welch',
            field=models.FloatField(blank=True, null=True, verbose_name='Power VLF Welch'),
        ),
        migrations.AlterField(
            model_name='hrvfreq',
            name='ttlpwr_lomb_ms2',
            field=models.FloatField(blank=True, null=True, verbose_name='TTLPWR Lomb Ms2'),
        ),
        migrations.AlterField(
            model_name='hrvfreq',
            name='ttlpwr_welch',
            field=models.FloatField(blank=True, null=True, verbose_name='TTLPWR Welch'),
        ),
        migrations.AlterField(
            model_name='hrvfreq',
            name='ulf_lomb_log',
            field=models.FloatField(blank=True, null=True, verbose_name='ULF Lomb Log'),
        ),
        migrations.AlterField(
            model_name='hrvfreq',
            name='ulf_lomb_ms2',
            field=models.FloatField(blank=True, null=True, verbose_name='Ultra Low Frequency Lomb (≤0.003 Hz)'),
        ),
        migrations.AlterField(
            model_name='hrvfreq',
            name='ulf_welch',
            field=models.FloatField(blank=True, null=True, verbose_name='ULF Welch'),
        ),
        migrations.AlterField(
            model_name='hrvfreq',
            name='vlf_lomb_log',
            field=models.FloatField(blank=True, null=True, verbose_name='VLF Lomb Log'),
        ),
        migrations.AlterField(
            model_name='hrvfreq',
            name='vlf_lomb_ms2',
            field=models.FloatField(blank=True, null=True, verbose_name='Very Low Frequency Lomb (0.0033–0.04 Hz)'),
        ),
        migrations.AlterField(
            model_name='hrvfreq',
            name='vlf_welch',
            field=models.FloatField(blank=True, null=True, verbose_name='VLF Welch'),
        ),
        migrations.AlterField(
            model_name='hrvnonlinear',
            name='alpha1',
            field=models.FloatField(blank=True, null=True, verbose_name='Alpha 1'),
        ),
        migrations.AlterField(
            model_name='hrvnonlinear',
            name='alpha2',
            field=models.FloatField(blank=True, null=True, verbose_name='Alpha 2'),
        ),
        migrations.AlterField(
            model_name='hrvnonlinear',
            name='area_sodp_rr',
            field=models.FloatField(blank=True, null=True, verbose_name='Area Sodp RR'),
        ),
        migrations.AlterField(
            model_name='hrvnonlinear',
            name='area_sodp_rr_log',
            field=models.FloatField(blank=True, null=True, verbose_name='Area Sodp RR (log)'),
        ),
        migrations.AlterField(
            model_name='hrvnonlinear',
            name='collectdata_non_lin',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='patient.CollectData', verbose_name='Collectdata Non_Lin'),
        ),
        migrations.AlterField(
            model_name='hrvnonlinear',
            name='collected_data',
            field=models.DateTimeField(default=django.utils.timezone.now, verbose_name='Collected Data'),
        ),
        migrations.AlterField(
            model_name='hrvnonlinear',
            name='csi',
            field=models.FloatField(blank=True, null=True, verbose_name='Cardiac Sympathetic Index'),
        ),
        migrations.AlterField(
            model_name='hrvnonlinear',
            name='ctm_r1',
            field=models.FloatField(blank=True, null=True, verbose_name='Ctm R1 (r = 10)'),
        ),
        migrations.AlterField(
            model_name='hrvnonlinear',
            name='ctm_r2',
            field=models.FloatField(blank=True, null=True, verbose_name='Ctm R2 (r = 20)'),
        ),
        migrations.AlterField(
            model_name='hrvnonlinear',
            name='ctm_r3',
            field=models.FloatField(blank=True, null=True, verbose_name='Ctm R3 (r = 40)'),
        ),
        migrations.AlterField(
            model_name='hrvnonlinear',
            name='cvi',
            field=models.FloatField(blank=True, null=True, verbose_name='Cardiac Vagal Index'),
        ),
        migrations.AlterField(
            model_name='hrvnonlinear',
            name='d2_10',
            field=models.FloatField(blank=True, null=True, verbose_name='D2 (dimension 10)'),
        ),
        migrations.AlterField(
            model_name='hrvnonlinear',
            name='d2_20',
            field=models.FloatField(blank=True, null=True, verbose_name='D2 (dimension 20)'),
        ),
        migrations.AlterField(
            model_name='hrvnonlinear',
            name='ellipse_area',
            field=models.FloatField(blank=True, null=True, verbose_name='Ellipse Area'),
        ),
        migrations.AlterField(
            model_name='hrvnonlinear',
            name='ent_amostra_1',
            field=models.FloatField(blank=True, null=True, verbose_name='Entropy Amostra_1'),
        ),
        migrations.AlterField(
            model_name='hrvnonlinear',
            name='ent_amostra_2',
            field=models.FloatField(blank=True, null=True, verbose_name='Entropy Amostra_2'),
        ),
        migrations.AlterField(
            model_name='hrvnonlinear',
            name='ent_aprox_1_01',
            field=models.FloatField(blank=True, null=True, verbose_name='Entropy Aprox_1_01'),
        ),
        migrations.AlterField(
            model_name='hrvnonlinear',
            name='ent_aprox_1_015',
            field=models.FloatField(blank=True, null=True, verbose_name='Entropy Aprox_1_015'),
        ),
        migrations.AlterField(
            model_name='hrvnonlinear',
            name='ent_aprox_1_02',
            field=models.FloatField(blank=True, null=True, verbose_name='Entropy Aprox_1_02'),
        ),
        migrations.AlterField(
            model_name='hrvnonlinear',
            name='ent_aprox_1_025',
            field=models.FloatField(blank=True, null=True, verbose_name='Entropy Aprox_1_025'),
        ),
        migrations.AlterField(
            model_name='hrvnonlinear',
            name='ent_aprox_2_01',
            field=models.FloatField(blank=True, null=True, verbose_name='Entropy Aprox_2_01'),
        ),
        migrations.AlterField(
            model_name='hrvnonlinear',
            name='ent_aprox_2_015',
            field=models.FloatField(blank=True, null=True, verbose_name='Entropy Aprox_2_015'),
        ),
        migrations.AlterField(
            model_name='hrvnonlinear',
            name='ent_aprox_2_02',
            field=models.FloatField(blank=True, null=True, verbose_name='Entropy Aprox_2_02'),
        ),
        migrations.AlterField(
            model_name='hrvnonlinear',
            name='ent_aprox_2_025',
            field=models.FloatField(blank=True, null=True, verbose_name='Entropy Aprox_2_025'),
        ),
        migrations.AlterField(
            model_name='hrvnonlinear',
            name='ent_conditional',
            field=models.FloatField(blank=True, null=True, verbose_name='Entropy Conditional'),
        ),
        migrations.AlterField(
            model_name='hrvnonlinear',
            name='ent_corrected_cond',
            field=models.FloatField(blank=True, null=True, verbose_name='Entropy Corrected_Cond'),
        ),
        migrations.AlterField(
            model_name='hrvnonlinear',
            name='ent_fuzzy',
            field=models.FloatField(blank=True, null=True, verbose_name='Entropy Fuzzy'),
        ),
        migrations.AlterField(
            model_name='hrvnonlinear',
            name='ent_multiescala_e3',
            field=models.FloatField(blank=True, null=True, verbose_name='Entropy Multiescala_E3'),
        ),
        migrations.AlterField(
            model_name='hrvnonlinear',
            name='ent_multiescala_e5',
            field=models.FloatField(blank=True, null=True, verbose_name='Entropy Multiescala_E5'),
        ),
        migrations.AlterField(
            model_name='hrvnonlinear',
            name='ent_permutation_1',
            field=models.FloatField(blank=True, null=True, verbose_name='Entropy Permutation_1'),
        ),
        migrations.AlterField(
            model_name='hrvnonlinear',
            name='ent_permutation_2',
            field=models.FloatField(blank=True, null=True, verbose_name='Entropy Permutation_2'),
        ),
        migrations.AlterField(
            model_name='hrvnonlinear',
            name='ent_shannon_1',
            field=models.FloatField(blank=True, null=True, verbose_name='Entropy Shannon1'),
        ),
        migrations.AlterField(
            model_name='hrvnonlinear',
            name='ent_shannon_2',
            field=models.FloatField(blank=True, null=True, verbose_name='Entropy Shannon_2'),
        ),
        migrations.AlterField(
            model_name='hrvnonlinear',
            name='ent_spectral',
            field=models.FloatField(blank=True, null=True, verbose_name='Entropy Spectral'),
        ),
        migrations.AlterField(
            model_name='hrvnonlinear',
            name='mean_dr1',
            field=models.FloatField(blank=True, null=True, verbose_name='Mean Dr1 (r = 10)'),
        ),
        migrations.AlterField(
            model_name='hrvnonlinear',
            name='mean_dr2',
            field=models.FloatField(blank=True, null=True, verbose_name='Mean Dr2 (r = 20)'),
        ),
        migrations.AlterField(
            model_name='hrvnonlinear',
            name='mean_dr3',
            field=models.FloatField(blank=True, null=True, verbose_name='Mean Dr3 (r = 40)'),
        ),
        migrations.AlterField(
            model_name='hrvnonlinear',
            name='mean_dr4',
            field=models.FloatField(blank=True, null=True, verbose_name='Mean Dr4 (r = 60)'),
        ),
        migrations.AlterField(
            model_name='hrvnonlinear',
            name='mean_dr5',
            field=models.FloatField(blank=True, null=True, verbose_name='Mean Dr5 (r = 80)'),
        ),
        migrations.AlterField(
            model_name='hrvnonlinear',
            name='norm_entropy',
            field=models.FloatField(blank=True, null=True, verbose_name='Norm Entropy'),
        ),
        migrations.AlterField(
            model_name='hrvnonlinear',
            name='sd1',
            field=models.FloatField(blank=True, null=True, verbose_name='Standard Deviation Perpendicular'),
        ),
        migrations.AlterField(
            model_name='hrvnonlinear',
            name='sd1_sd2_ratio',
            field=models.FloatField(blank=True, null=True, verbose_name='SD_Perp SD_Along Ratio'),
        ),
        migrations.AlterField(
            model_name='hrvnonlinear',
            name='sd2',
            field=models.FloatField(blank=True, null=True, verbose_name='Standard Deviation Along'),
        ),
        migrations.AlterField(
            model_name='hrvtime',
            name='collectdata_time',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='patient.CollectData', verbose_name='Collect Data Time'),
        ),
        migrations.AlterField(
            model_name='hrvtime',
            name='collected_data',
            field=models.DateTimeField(default=django.utils.timezone.now, verbose_name='Collected Data'),
        ),
        migrations.AlterField(
            model_name='hrvtime',
            name='cv',
            field=models.FloatField(blank=True, null=True, verbose_name='Coefficient Variation'),
        ),
        migrations.AlterField(
            model_name='hrvtime',
            name='nn20',
            field=models.FloatField(blank=True, null=True, verbose_name='NN (20ms)'),
        ),
        migrations.AlterField(
            model_name='hrvtime',
            name='nn50',
            field=models.FloatField(blank=True, null=True, verbose_name='NN (50ms)'),
        ),
        migrations.AlterField(
            model_name='hrvtime',
            name='nn_iqr',
            field=models.FloatField(blank=True, null=True, verbose_name='NN Interquartile'),
        ),
        migrations.AlterField(
            model_name='hrvtime',
            name='nn_kurt',
            field=models.FloatField(blank=True, null=True, verbose_name='NN Kurtosis'),
        ),
        migrations.AlterField(
            model_name='hrvtime',
            name='nn_skew',
            field=models.FloatField(blank=True, null=True, verbose_name='NN Skewness'),
        ),
        migrations.AlterField(
            model_name='hrvtime',
            name='pnn20_pr',
            field=models.FloatField(blank=True, null=True, verbose_name='pNN (20ms) pr '),
        ),
        migrations.AlterField(
            model_name='hrvtime',
            name='pnn50_pr',
            field=models.FloatField(blank=True, null=True, verbose_name='pNN (50ms) pr'),
        ),
        migrations.AlterField(
            model_name='hrvtime',
            name='sd_nn',
            field=models.FloatField(blank=True, null=True, verbose_name='SD NN'),
        ),
        migrations.AlterField(
            model_name='hrvtime',
            name='sdsd',
            field=models.FloatField(blank=True, null=True, verbose_name='SDSD'),
        ),
    ]
