# Generated by Django 4.0.3 on 2022-04-14 00:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main_page', '0012_alter_transfer_accounts'),
    ]

    operations = [
        migrations.AddField(
            model_name='transfer',
            name='name',
            field=models.CharField(max_length=30, null=True),
        ),
    ]
