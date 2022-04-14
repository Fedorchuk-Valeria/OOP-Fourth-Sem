# Generated by Django 4.0.3 on 2022-04-11 04:04

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('main_page', '0008_transfer'),
        ('office', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Operator',
            fields=[
                ('user_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='main_page.user')),
            ],
            bases=('main_page.user',),
        ),
        migrations.CreateModel(
            name='Manager',
            fields=[
                ('operator_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='office.operator')),
            ],
            bases=('office.operator',),
        ),
    ]