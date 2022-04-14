# Generated by Django 4.0.3 on 2022-04-09 23:47

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('main_page', '0002_bank_user'),
    ]

    operations = [
        migrations.CreateModel(
            name='Account',
            fields=[
                ('money', models.IntegerField(null=True)),
                ('date_of_creation', models.DateField(auto_now=True, null=True)),
                ('number', models.CharField(default='-1', max_length=10, primary_key=True, serialize=False)),
                ('current', models.BooleanField(default=False)),
                ('bank', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='main_page.bank')),
                ('user', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='main_page.user')),
            ],
        ),
    ]
