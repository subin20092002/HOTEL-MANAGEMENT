# Generated by Django 5.0.1 on 2024-03-10 06:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('frontend', '0019_alter_checkout_status'),
    ]

    operations = [
        migrations.RenameField(
            model_name='signupdb',
            old_name='address',
            new_name='City',
        ),
        migrations.AddField(
            model_name='signupdb',
            name='House_No',
            field=models.CharField(blank=True, max_length=250, null=True),
        ),
        migrations.AddField(
            model_name='signupdb',
            name='Pincode',
            field=models.CharField(blank=True, max_length=250, null=True),
        ),
        migrations.AddField(
            model_name='signupdb',
            name='street',
            field=models.CharField(blank=True, max_length=250, null=True),
        ),
    ]
