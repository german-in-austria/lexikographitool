# Generated by Django 3.1.4 on 2021-03-29 17:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('lexeme', '0003_address_country'),
    ]

    operations = [
        migrations.AlterField(
            model_name='address',
            name='osm_id',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
    ]
