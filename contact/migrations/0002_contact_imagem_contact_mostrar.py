# Generated by Django 5.0.4 on 2024-04-05 13:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('contact', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='contact',
            name='imagem',
            field=models.ImageField(blank=True, upload_to='imagens/%y/%m/'),
        ),
        migrations.AddField(
            model_name='contact',
            name='mostrar',
            field=models.BooleanField(default=True),
        ),
    ]
