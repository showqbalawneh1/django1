# Generated by Django 3.1 on 2022-09-11 16:20

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('sensor', '0006_auto_20220911_1535'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pressuresensor',
            name='serial_number',
            field=models.CharField(default=uuid.uuid4, max_length=200, unique=True),
        ),
    ]
