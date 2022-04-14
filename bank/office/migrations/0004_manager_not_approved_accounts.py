# Generated by Django 4.0.3 on 2022-04-11 11:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main_page', '0008_transfer'),
        ('office', '0003_manager_on_work'),
    ]

    operations = [
        migrations.AddField(
            model_name='manager',
            name='not_approved_accounts',
            field=models.ManyToManyField(to='main_page.account'),
        ),
    ]
