# Generated by Django 4.0.4 on 2022-04-12 16:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('projects', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='project',
            name='image',
            field=models.ImageField(upload_to='projects/static/img'),
        ),
    ]
