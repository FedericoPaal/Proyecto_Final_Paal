# Generated by Django 4.2.4 on 2023-10-05 19:36

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('App_Tercera_Pre_Entrega_Paal', '0008_producto_creacion_producto_texto'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='consultas_clientes',
            name='consulta_cliente',
        ),
        migrations.DeleteModel(
            name='Avatar',
        ),
        migrations.DeleteModel(
            name='Consultas_Clientes',
        ),
    ]