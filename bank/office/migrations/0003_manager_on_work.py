# Generated by Django 4.0.3 on 2022-04-11 06:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('office', '0002_operator_manager'),
    ]

    operations = [
        migrations.AddField(
            model_name='manager',
            name='on_work',
            field=models.BooleanField(default=False),
        ),
    ]
