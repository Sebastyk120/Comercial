# Generated by Django 5.0 on 2023-12-18 04:20

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('inventarios', '0002_inventario_propiedad_heavens_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='inventario',
            name='propiedad_heavens',
        ),
    ]
