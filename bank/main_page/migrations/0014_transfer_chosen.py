# Generated by Django 4.0.3 on 2022-04-14 00:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main_page', '0013_transfer_name'),
    ]

    operations = [
        migrations.AddField(
            model_name='transfer',
            name='chosen',
            field=models.BooleanField(default=False),
        ),
    ]