# Generated by Django 4.0.3 on 2022-04-15 12:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main_page', '0015_installment_credit'),
        ('office', '0006_operator_operations'),
    ]

    operations = [
        migrations.AddField(
            model_name='manager',
            name='not_approved_installments',
            field=models.ManyToManyField(to='main_page.installment'),
        ),
    ]
