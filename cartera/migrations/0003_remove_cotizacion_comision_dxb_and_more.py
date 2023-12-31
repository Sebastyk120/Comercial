# Generated by Django 5.0 on 2023-12-30 00:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cartera', '0002_cotizacion_trm_cotizacion'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='cotizacion',
            name='comision_dxb',
        ),
        migrations.RemoveField(
            model_name='cotizacion',
            name='comision_fob',
        ),
        migrations.AddField(
            model_name='cotizacion',
            name='comi_ams',
            field=models.DecimalField(blank=True, decimal_places=2, max_digits=10, null=True, verbose_name='Com AMS'),
        ),
        migrations.AddField(
            model_name='cotizacion',
            name='comi_ayt',
            field=models.DecimalField(blank=True, decimal_places=2, max_digits=10, null=True, verbose_name='Com AYT'),
        ),
        migrations.AddField(
            model_name='cotizacion',
            name='comi_bah',
            field=models.DecimalField(blank=True, decimal_places=2, max_digits=10, null=True, verbose_name='Com BAH'),
        ),
        migrations.AddField(
            model_name='cotizacion',
            name='comi_bcn',
            field=models.DecimalField(blank=True, decimal_places=2, max_digits=10, null=True, verbose_name='Com BCN'),
        ),
        migrations.AddField(
            model_name='cotizacion',
            name='comi_bey',
            field=models.DecimalField(blank=True, decimal_places=2, max_digits=10, null=True, verbose_name='Com BEY'),
        ),
        migrations.AddField(
            model_name='cotizacion',
            name='comi_cdg',
            field=models.DecimalField(blank=True, decimal_places=2, max_digits=10, null=True, verbose_name='Com CDG'),
        ),
        migrations.AddField(
            model_name='cotizacion',
            name='comi_cgk',
            field=models.DecimalField(blank=True, decimal_places=2, max_digits=10, null=True, verbose_name='Com CGK'),
        ),
        migrations.AddField(
            model_name='cotizacion',
            name='comi_dmm',
            field=models.DecimalField(blank=True, decimal_places=2, max_digits=10, null=True, verbose_name='Com DMM'),
        ),
        migrations.AddField(
            model_name='cotizacion',
            name='comi_doh',
            field=models.DecimalField(blank=True, decimal_places=2, max_digits=10, null=True, verbose_name='Com DOH'),
        ),
        migrations.AddField(
            model_name='cotizacion',
            name='comi_dxb',
            field=models.DecimalField(blank=True, decimal_places=2, max_digits=10, null=True, verbose_name='Com DXB'),
        ),
        migrations.AddField(
            model_name='cotizacion',
            name='comi_edi',
            field=models.DecimalField(blank=True, decimal_places=2, max_digits=10, null=True, verbose_name='Com EDI'),
        ),
        migrations.AddField(
            model_name='cotizacion',
            name='comi_fob',
            field=models.DecimalField(blank=True, decimal_places=2, max_digits=10, null=True, verbose_name='Com FOB'),
        ),
        migrations.AddField(
            model_name='cotizacion',
            name='comi_fra',
            field=models.DecimalField(blank=True, decimal_places=2, max_digits=10, null=True, verbose_name='Com FRA'),
        ),
        migrations.AddField(
            model_name='cotizacion',
            name='comi_gua',
            field=models.DecimalField(blank=True, decimal_places=2, max_digits=10, null=True, verbose_name='Com GUA'),
        ),
        migrations.AddField(
            model_name='cotizacion',
            name='comi_hkg',
            field=models.DecimalField(blank=True, decimal_places=2, max_digits=10, null=True, verbose_name='Com HKG'),
        ),
        migrations.AddField(
            model_name='cotizacion',
            name='comi_jed',
            field=models.DecimalField(blank=True, decimal_places=2, max_digits=10, null=True, verbose_name='Com JED'),
        ),
        migrations.AddField(
            model_name='cotizacion',
            name='comi_kbp',
            field=models.DecimalField(blank=True, decimal_places=2, max_digits=10, null=True, verbose_name='Com KBP'),
        ),
        migrations.AddField(
            model_name='cotizacion',
            name='comi_kul',
            field=models.DecimalField(blank=True, decimal_places=2, max_digits=10, null=True, verbose_name='Com KUL'),
        ),
        migrations.AddField(
            model_name='cotizacion',
            name='comi_kwi',
            field=models.DecimalField(blank=True, decimal_places=2, max_digits=10, null=True, verbose_name='Com KWI'),
        ),
        migrations.AddField(
            model_name='cotizacion',
            name='comi_lgg',
            field=models.DecimalField(blank=True, decimal_places=2, max_digits=10, null=True, verbose_name='Com LGG'),
        ),
        migrations.AddField(
            model_name='cotizacion',
            name='comi_lhr',
            field=models.DecimalField(blank=True, decimal_places=2, max_digits=10, null=True, verbose_name='Com LHR'),
        ),
        migrations.AddField(
            model_name='cotizacion',
            name='comi_mad',
            field=models.DecimalField(blank=True, decimal_places=2, max_digits=10, null=True, verbose_name='Com MAD'),
        ),
        migrations.AddField(
            model_name='cotizacion',
            name='comi_mtc',
            field=models.DecimalField(blank=True, decimal_places=2, max_digits=10, null=True, verbose_name='Com MTC'),
        ),
        migrations.AddField(
            model_name='cotizacion',
            name='comi_mxp',
            field=models.DecimalField(blank=True, decimal_places=2, max_digits=10, null=True, verbose_name='Com MXP'),
        ),
        migrations.AddField(
            model_name='cotizacion',
            name='comi_ruh',
            field=models.DecimalField(blank=True, decimal_places=2, max_digits=10, null=True, verbose_name='Com RUH'),
        ),
        migrations.AddField(
            model_name='cotizacion',
            name='comi_sin',
            field=models.DecimalField(blank=True, decimal_places=2, max_digits=10, null=True, verbose_name='Com SIN'),
        ),
        migrations.AddField(
            model_name='cotizacion',
            name='comi_svo',
            field=models.DecimalField(blank=True, decimal_places=2, max_digits=10, null=True, verbose_name='Com SVO'),
        ),
        migrations.AddField(
            model_name='cotizacion',
            name='comi_vko',
            field=models.DecimalField(blank=True, decimal_places=2, max_digits=10, null=True, verbose_name='Com VKO'),
        ),
        migrations.AddField(
            model_name='cotizacion',
            name='comi_yul',
            field=models.DecimalField(blank=True, decimal_places=2, max_digits=10, null=True, verbose_name='Com YUL'),
        ),
        migrations.AddField(
            model_name='cotizacion',
            name='comi_yvr',
            field=models.DecimalField(blank=True, decimal_places=2, max_digits=10, null=True, verbose_name='Com YVR'),
        ),
        migrations.AddField(
            model_name='cotizacion',
            name='comi_yyz',
            field=models.DecimalField(blank=True, decimal_places=2, max_digits=10, null=True, verbose_name='Com YYZ'),
        ),
        migrations.AddField(
            model_name='cotizacion',
            name='comi_zhr',
            field=models.DecimalField(blank=True, decimal_places=2, max_digits=10, null=True, verbose_name='Com ZHR'),
        ),
        migrations.AddField(
            model_name='cotizacion',
            name='precio_ams',
            field=models.DecimalField(blank=True, decimal_places=2, max_digits=10, null=True, verbose_name='$AMS'),
        ),
        migrations.AddField(
            model_name='cotizacion',
            name='precio_ayt',
            field=models.DecimalField(blank=True, decimal_places=2, max_digits=10, null=True, verbose_name='$AYT'),
        ),
        migrations.AddField(
            model_name='cotizacion',
            name='precio_bah',
            field=models.DecimalField(blank=True, decimal_places=2, max_digits=10, null=True, verbose_name='$BAH'),
        ),
        migrations.AddField(
            model_name='cotizacion',
            name='precio_bcn',
            field=models.DecimalField(blank=True, decimal_places=2, max_digits=10, null=True, verbose_name='$BCN'),
        ),
        migrations.AddField(
            model_name='cotizacion',
            name='precio_bey',
            field=models.DecimalField(blank=True, decimal_places=2, max_digits=10, null=True, verbose_name='$BEY'),
        ),
        migrations.AddField(
            model_name='cotizacion',
            name='precio_cdg',
            field=models.DecimalField(blank=True, decimal_places=2, max_digits=10, null=True, verbose_name='$CDG'),
        ),
        migrations.AddField(
            model_name='cotizacion',
            name='precio_cgk',
            field=models.DecimalField(blank=True, decimal_places=2, max_digits=10, null=True, verbose_name='$CGK'),
        ),
        migrations.AddField(
            model_name='cotizacion',
            name='precio_dmm',
            field=models.DecimalField(blank=True, decimal_places=2, max_digits=10, null=True, verbose_name='$DMM'),
        ),
        migrations.AddField(
            model_name='cotizacion',
            name='precio_doh',
            field=models.DecimalField(blank=True, decimal_places=2, max_digits=10, null=True, verbose_name='$DOH'),
        ),
        migrations.AddField(
            model_name='cotizacion',
            name='precio_edi',
            field=models.DecimalField(blank=True, decimal_places=2, max_digits=10, null=True, verbose_name='$EDI'),
        ),
        migrations.AddField(
            model_name='cotizacion',
            name='precio_fra',
            field=models.DecimalField(blank=True, decimal_places=2, max_digits=10, null=True, verbose_name='$FRA'),
        ),
        migrations.AddField(
            model_name='cotizacion',
            name='precio_gua',
            field=models.DecimalField(blank=True, decimal_places=2, max_digits=10, null=True, verbose_name='$GUA'),
        ),
        migrations.AddField(
            model_name='cotizacion',
            name='precio_hkg',
            field=models.DecimalField(blank=True, decimal_places=2, max_digits=10, null=True, verbose_name='$HKG'),
        ),
        migrations.AddField(
            model_name='cotizacion',
            name='precio_jed',
            field=models.DecimalField(blank=True, decimal_places=2, max_digits=10, null=True, verbose_name='$JED'),
        ),
        migrations.AddField(
            model_name='cotizacion',
            name='precio_kbp',
            field=models.DecimalField(blank=True, decimal_places=2, max_digits=10, null=True, verbose_name='$KBP'),
        ),
        migrations.AddField(
            model_name='cotizacion',
            name='precio_kul',
            field=models.DecimalField(blank=True, decimal_places=2, max_digits=10, null=True, verbose_name='$KUL'),
        ),
        migrations.AddField(
            model_name='cotizacion',
            name='precio_kwi',
            field=models.DecimalField(blank=True, decimal_places=2, max_digits=10, null=True, verbose_name='$KWI'),
        ),
        migrations.AddField(
            model_name='cotizacion',
            name='precio_lgg',
            field=models.DecimalField(blank=True, decimal_places=2, max_digits=10, null=True, verbose_name='$LGG'),
        ),
        migrations.AddField(
            model_name='cotizacion',
            name='precio_lhr',
            field=models.DecimalField(blank=True, decimal_places=2, max_digits=10, null=True, verbose_name='$LHR'),
        ),
        migrations.AddField(
            model_name='cotizacion',
            name='precio_mad',
            field=models.DecimalField(blank=True, decimal_places=2, max_digits=10, null=True, verbose_name='$MAD'),
        ),
        migrations.AddField(
            model_name='cotizacion',
            name='precio_mtc',
            field=models.DecimalField(blank=True, decimal_places=2, max_digits=10, null=True, verbose_name='$MTC'),
        ),
        migrations.AddField(
            model_name='cotizacion',
            name='precio_mxp',
            field=models.DecimalField(blank=True, decimal_places=2, max_digits=10, null=True, verbose_name='$MXP'),
        ),
        migrations.AddField(
            model_name='cotizacion',
            name='precio_ruh',
            field=models.DecimalField(blank=True, decimal_places=2, max_digits=10, null=True, verbose_name='$RUH'),
        ),
        migrations.AddField(
            model_name='cotizacion',
            name='precio_sin',
            field=models.DecimalField(blank=True, decimal_places=2, max_digits=10, null=True, verbose_name='$SIN'),
        ),
        migrations.AddField(
            model_name='cotizacion',
            name='precio_svo',
            field=models.DecimalField(blank=True, decimal_places=2, max_digits=10, null=True, verbose_name='$SVO'),
        ),
        migrations.AddField(
            model_name='cotizacion',
            name='precio_vko',
            field=models.DecimalField(blank=True, decimal_places=2, max_digits=10, null=True, verbose_name='$VKO'),
        ),
        migrations.AddField(
            model_name='cotizacion',
            name='precio_yul',
            field=models.DecimalField(blank=True, decimal_places=2, max_digits=10, null=True, verbose_name='$YUL'),
        ),
        migrations.AddField(
            model_name='cotizacion',
            name='precio_yvr',
            field=models.DecimalField(blank=True, decimal_places=2, max_digits=10, null=True, verbose_name='$YVR'),
        ),
        migrations.AddField(
            model_name='cotizacion',
            name='precio_yyz',
            field=models.DecimalField(blank=True, decimal_places=2, max_digits=10, null=True, verbose_name='$YYZ'),
        ),
        migrations.AddField(
            model_name='cotizacion',
            name='precio_zhr',
            field=models.DecimalField(blank=True, decimal_places=2, max_digits=10, null=True, verbose_name='$ZHR'),
        ),
        migrations.AlterField(
            model_name='cotizacion',
            name='precio_dxb',
            field=models.DecimalField(blank=True, decimal_places=2, max_digits=10, null=True, verbose_name='$DXB'),
        ),
        migrations.AlterField(
            model_name='cotizacion',
            name='precio_fob',
            field=models.DecimalField(blank=True, decimal_places=2, max_digits=10, null=True, verbose_name='$FOB'),
        ),
    ]
