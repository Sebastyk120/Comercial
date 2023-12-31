# Generated by Django 5.0 on 2023-12-30 22:27

import django.core.validators
import django.db.models.deletion
import simple_history.models
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cartera', '0004_rename_cotizacion_cotizacionetnico'),
        ('comercial', '0006_alter_historicalpedido_tasa_representativa_usd_diaria_and_more'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='HistoricalCotizacionEtnico',
            fields=[
                ('id', models.BigIntegerField(auto_created=True, blank=True, db_index=True, verbose_name='ID')),
                ('semana', models.IntegerField(validators=[django.core.validators.MinValueValidator(1), django.core.validators.MaxValueValidator(56)], verbose_name='Semana')),
                ('trm_cotizacion', models.DecimalField(blank=True, decimal_places=2, max_digits=10, null=True, validators=[django.core.validators.MinValueValidator(0)], verbose_name='TRM Cotizacion')),
                ('precio_fob', models.DecimalField(blank=True, decimal_places=2, max_digits=10, null=True, verbose_name='$FOB')),
                ('comi_fob', models.DecimalField(blank=True, decimal_places=2, max_digits=10, null=True, verbose_name='Com FOB')),
                ('precio_dxb', models.DecimalField(blank=True, decimal_places=2, max_digits=10, null=True, verbose_name='$DXB')),
                ('comi_dxb', models.DecimalField(blank=True, decimal_places=2, max_digits=10, null=True, verbose_name='Com DXB')),
                ('precio_doh', models.DecimalField(blank=True, decimal_places=2, max_digits=10, null=True, verbose_name='$DOH')),
                ('comi_doh', models.DecimalField(blank=True, decimal_places=2, max_digits=10, null=True, verbose_name='Com DOH')),
                ('precio_bah', models.DecimalField(blank=True, decimal_places=2, max_digits=10, null=True, verbose_name='$BAH')),
                ('comi_bah', models.DecimalField(blank=True, decimal_places=2, max_digits=10, null=True, verbose_name='Com BAH')),
                ('precio_kwi', models.DecimalField(blank=True, decimal_places=2, max_digits=10, null=True, verbose_name='$KWI')),
                ('comi_kwi', models.DecimalField(blank=True, decimal_places=2, max_digits=10, null=True, verbose_name='Com KWI')),
                ('precio_ruh', models.DecimalField(blank=True, decimal_places=2, max_digits=10, null=True, verbose_name='$RUH')),
                ('comi_ruh', models.DecimalField(blank=True, decimal_places=2, max_digits=10, null=True, verbose_name='Com RUH')),
                ('precio_jed', models.DecimalField(blank=True, decimal_places=2, max_digits=10, null=True, verbose_name='$JED')),
                ('comi_jed', models.DecimalField(blank=True, decimal_places=2, max_digits=10, null=True, verbose_name='Com JED')),
                ('precio_svo', models.DecimalField(blank=True, decimal_places=2, max_digits=10, null=True, verbose_name='$SVO')),
                ('comi_svo', models.DecimalField(blank=True, decimal_places=2, max_digits=10, null=True, verbose_name='Com SVO')),
                ('precio_lhr', models.DecimalField(blank=True, decimal_places=2, max_digits=10, null=True, verbose_name='$LHR')),
                ('comi_lhr', models.DecimalField(blank=True, decimal_places=2, max_digits=10, null=True, verbose_name='Com LHR')),
                ('precio_ams', models.DecimalField(blank=True, decimal_places=2, max_digits=10, null=True, verbose_name='$AMS')),
                ('comi_ams', models.DecimalField(blank=True, decimal_places=2, max_digits=10, null=True, verbose_name='Com AMS')),
                ('precio_mad', models.DecimalField(blank=True, decimal_places=2, max_digits=10, null=True, verbose_name='$MAD')),
                ('comi_mad', models.DecimalField(blank=True, decimal_places=2, max_digits=10, null=True, verbose_name='Com MAD')),
                ('precio_mxp', models.DecimalField(blank=True, decimal_places=2, max_digits=10, null=True, verbose_name='$MXP')),
                ('comi_mxp', models.DecimalField(blank=True, decimal_places=2, max_digits=10, null=True, verbose_name='Com MXP')),
                ('precio_vko', models.DecimalField(blank=True, decimal_places=2, max_digits=10, null=True, verbose_name='$VKO')),
                ('comi_vko', models.DecimalField(blank=True, decimal_places=2, max_digits=10, null=True, verbose_name='Com VKO')),
                ('precio_cdg', models.DecimalField(blank=True, decimal_places=2, max_digits=10, null=True, verbose_name='$CDG')),
                ('comi_cdg', models.DecimalField(blank=True, decimal_places=2, max_digits=10, null=True, verbose_name='Com CDG')),
                ('precio_kbp', models.DecimalField(blank=True, decimal_places=2, max_digits=10, null=True, verbose_name='$KBP')),
                ('comi_kbp', models.DecimalField(blank=True, decimal_places=2, max_digits=10, null=True, verbose_name='Com KBP')),
                ('precio_yul', models.DecimalField(blank=True, decimal_places=2, max_digits=10, null=True, verbose_name='$YUL')),
                ('comi_yul', models.DecimalField(blank=True, decimal_places=2, max_digits=10, null=True, verbose_name='Com YUL')),
                ('precio_yyz', models.DecimalField(blank=True, decimal_places=2, max_digits=10, null=True, verbose_name='$YYZ')),
                ('comi_yyz', models.DecimalField(blank=True, decimal_places=2, max_digits=10, null=True, verbose_name='Com YYZ')),
                ('precio_yvr', models.DecimalField(blank=True, decimal_places=2, max_digits=10, null=True, verbose_name='$YVR')),
                ('comi_yvr', models.DecimalField(blank=True, decimal_places=2, max_digits=10, null=True, verbose_name='Com YVR')),
                ('precio_edi', models.DecimalField(blank=True, decimal_places=2, max_digits=10, null=True, verbose_name='$EDI')),
                ('comi_edi', models.DecimalField(blank=True, decimal_places=2, max_digits=10, null=True, verbose_name='Com EDI')),
                ('precio_zhr', models.DecimalField(blank=True, decimal_places=2, max_digits=10, null=True, verbose_name='$ZHR')),
                ('comi_zhr', models.DecimalField(blank=True, decimal_places=2, max_digits=10, null=True, verbose_name='Com ZHR')),
                ('precio_sin', models.DecimalField(blank=True, decimal_places=2, max_digits=10, null=True, verbose_name='$SIN')),
                ('comi_sin', models.DecimalField(blank=True, decimal_places=2, max_digits=10, null=True, verbose_name='Com SIN')),
                ('precio_fra', models.DecimalField(blank=True, decimal_places=2, max_digits=10, null=True, verbose_name='$FRA')),
                ('comi_fra', models.DecimalField(blank=True, decimal_places=2, max_digits=10, null=True, verbose_name='Com FRA')),
                ('precio_bcn', models.DecimalField(blank=True, decimal_places=2, max_digits=10, null=True, verbose_name='$BCN')),
                ('comi_bcn', models.DecimalField(blank=True, decimal_places=2, max_digits=10, null=True, verbose_name='Com BCN')),
                ('precio_lgg', models.DecimalField(blank=True, decimal_places=2, max_digits=10, null=True, verbose_name='$LGG')),
                ('comi_lgg', models.DecimalField(blank=True, decimal_places=2, max_digits=10, null=True, verbose_name='Com LGG')),
                ('precio_kul', models.DecimalField(blank=True, decimal_places=2, max_digits=10, null=True, verbose_name='$KUL')),
                ('comi_kul', models.DecimalField(blank=True, decimal_places=2, max_digits=10, null=True, verbose_name='Com KUL')),
                ('precio_hkg', models.DecimalField(blank=True, decimal_places=2, max_digits=10, null=True, verbose_name='$HKG')),
                ('comi_hkg', models.DecimalField(blank=True, decimal_places=2, max_digits=10, null=True, verbose_name='Com HKG')),
                ('precio_mtc', models.DecimalField(blank=True, decimal_places=2, max_digits=10, null=True, verbose_name='$MTC')),
                ('comi_mtc', models.DecimalField(blank=True, decimal_places=2, max_digits=10, null=True, verbose_name='Com MTC')),
                ('precio_bey', models.DecimalField(blank=True, decimal_places=2, max_digits=10, null=True, verbose_name='$BEY')),
                ('comi_bey', models.DecimalField(blank=True, decimal_places=2, max_digits=10, null=True, verbose_name='Com BEY')),
                ('precio_dmm', models.DecimalField(blank=True, decimal_places=2, max_digits=10, null=True, verbose_name='$DMM')),
                ('comi_dmm', models.DecimalField(blank=True, decimal_places=2, max_digits=10, null=True, verbose_name='Com DMM')),
                ('precio_gua', models.DecimalField(blank=True, decimal_places=2, max_digits=10, null=True, verbose_name='$GUA')),
                ('comi_gua', models.DecimalField(blank=True, decimal_places=2, max_digits=10, null=True, verbose_name='Com GUA')),
                ('precio_ayt', models.DecimalField(blank=True, decimal_places=2, max_digits=10, null=True, verbose_name='$AYT')),
                ('comi_ayt', models.DecimalField(blank=True, decimal_places=2, max_digits=10, null=True, verbose_name='Com AYT')),
                ('precio_cgk', models.DecimalField(blank=True, decimal_places=2, max_digits=10, null=True, verbose_name='$CGK')),
                ('comi_cgk', models.DecimalField(blank=True, decimal_places=2, max_digits=10, null=True, verbose_name='Com CGK')),
                ('history_id', models.AutoField(primary_key=True, serialize=False)),
                ('history_date', models.DateTimeField(db_index=True)),
                ('history_change_reason', models.CharField(max_length=100, null=True)),
                ('history_type', models.CharField(choices=[('+', 'Created'), ('~', 'Changed'), ('-', 'Deleted')], max_length=1)),
                ('history_user', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to=settings.AUTH_USER_MODEL)),
                ('presentacion', models.ForeignKey(blank=True, db_constraint=False, null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='+', to='comercial.presentacion')),
            ],
            options={
                'verbose_name': 'historical cotizacion etnico',
                'verbose_name_plural': 'historical cotizacion etnicos',
                'ordering': ('-history_date', '-history_id'),
                'get_latest_by': ('history_date', 'history_id'),
            },
            bases=(simple_history.models.HistoricalChanges, models.Model),
        ),
    ]
