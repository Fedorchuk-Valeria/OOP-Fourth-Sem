# Generated by Django 4.0.3 on 2022-04-11 00:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main_page', '0004_alter_user_online'),
    ]

    operations = [
        migrations.AddField(
            model_name='account',
            name='frozen',
            field=models.BooleanField(default=False),
        ),
    ]
