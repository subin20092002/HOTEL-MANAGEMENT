# Generated by Django 5.0.1 on 2024-03-10 07:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('frontend', '0022_review'),
    ]

    operations = [
        migrations.AlterField(
            model_name='review',
            name='rating',
            field=models.CharField(max_length=100),
        ),
    ]
