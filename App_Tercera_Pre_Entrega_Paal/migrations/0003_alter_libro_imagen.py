# Generated by Django 4.2.4 on 2023-10-02 19:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('App_Tercera_Pre_Entrega_Paal', '0002_alter_libro_imagen'),
    ]

    operations = [
        migrations.AlterField(
            model_name='libro',
            name='imagen',
            field=models.ImageField(blank=True, null=True, upload_to='Libros'),
        ),
    ]
