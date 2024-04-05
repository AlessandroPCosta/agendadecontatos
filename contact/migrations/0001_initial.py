# Generated by Django 5.0.4 on 2024-04-05 12:50

import django.utils.timezone
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Contact',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=50, verbose_name='Nome')),
                ('sobrenome', models.CharField(blank=True, max_length=50, verbose_name='Sobrenome')),
                ('phone', models.CharField(max_length=50, verbose_name='Phone')),
                ('email', models.EmailField(blank=True, max_length=250, verbose_name='E-mail')),
                ('create_data', models.DateTimeField(default=django.utils.timezone.now)),
                ('descrição', models.TextField(blank=True)),
            ],
        ),
    ]