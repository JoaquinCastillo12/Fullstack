# Generated by Django 5.2.1 on 2025-06-27 15:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0007_remove_producto_caracteristicas_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='fichatecnica',
            name='archivo_pdf',
            field=models.BinaryField(),
        ),
    ]
