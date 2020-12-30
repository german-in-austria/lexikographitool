# Generated by Django 3.1.3 on 2020-12-07 16:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='account',
            name='firstname',
            field=models.CharField(default='user', max_length=100),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='account',
            name='lastname',
            field=models.CharField(default='Mustermann', max_length=100),
            preserve_default=False,
        ),
    ]