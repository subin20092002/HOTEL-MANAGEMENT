# Generated by Django 4.2.6 on 2023-12-04 17:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('frontend', '0003_alter_signupdb_email_alter_signupdb_repeatpassword'),
    ]

    operations = [
        migrations.CreateModel(
            name='booktableDb',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=100, null=True)),
                ('number', models.IntegerField(blank=True, max_length=100, null=True)),
                ('email', models.EmailField(blank=True, max_length=100, null=True)),
                ('persons', models.IntegerField(blank=True, max_length=100, null=True)),
                ('date', models.DateField(blank=True, max_length=100, null=True)),
            ],
        ),
        migrations.RemoveField(
            model_name='signupdb',
            name='repeatpassword',
        ),
    ]