# Generated by Django 4.2.6 on 2023-11-17 15:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('inicio', '0008_alter_medias_anio'),
    ]

    operations = [
        migrations.AlterField(
            model_name='camiseta',
            name='equipo',
            field=models.CharField(max_length=30),
        ),
    ]
