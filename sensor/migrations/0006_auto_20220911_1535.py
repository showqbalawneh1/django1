# Generated by Django 3.1 on 2022-09-11 15:35

from django.db import migrations, models
import sensor.models


class Migration(migrations.Migration):

    dependencies = [
        ('sensor', '0005_auto_20220911_1352'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pressuresensor',
            name='labelSensor',
            field=models.CharField(max_length=200, validators=[sensor.models.pressureSensor.validation]),
        ),
    ]