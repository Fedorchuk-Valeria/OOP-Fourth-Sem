# Generated by Django 4.0.3 on 2022-04-11 01:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main_page', '0005_account_frozen'),
    ]

    operations = [
        migrations.CreateModel(
            name='Transfer',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('money', models.IntegerField(null=True)),
            ],
        ),
    ]
