# Generated by Django 5.0.1 on 2024-03-02 14:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('frontend', '0015_booktabledb_fromtime_booktabledb_totime_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='checkout',
            name='status',
            field=models.CharField(default='Pending', max_length=200),
        ),
    ]
