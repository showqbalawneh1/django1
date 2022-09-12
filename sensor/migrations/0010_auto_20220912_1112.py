# Generated by Django 3.1 on 2022-09-12 11:12

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('sensor', '0009_auto_20220912_1058'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pressuresensor',
            name='serial_number',
            field=models.CharField(default=uuid.uuid4, editable=False, max_length=200),
        ),
    ]