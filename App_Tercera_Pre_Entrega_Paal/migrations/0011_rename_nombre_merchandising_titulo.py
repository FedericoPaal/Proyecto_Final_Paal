# Generated by Django 4.2.4 on 2023-09-25 23:14

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('App_Tercera_Pre_Entrega_Paal', '0010_alter_libro_imagen_alter_merchandising_imagen_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='merchandising',
            old_name='nombre',
            new_name='titulo',
        ),
    ]