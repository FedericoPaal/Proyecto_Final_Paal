# Generated by Django 4.2.4 on 2023-10-04 03:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('App_Tercera_Pre_Entrega_Paal', '0006_libro_texto_merchandising_texto_novedad_texto'),
    ]

    operations = [
        migrations.AlterField(
            model_name='libro',
            name='creacion',
            field=models.DateField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='merchandising',
            name='creacion',
            field=models.DateField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='novedad',
            name='creacion',
            field=models.DateField(blank=True, null=True),
        ),
    ]