# Generated by Django 3.2.18 on 2023-03-09 20:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('logPage', '0006_auto_20230309_1451'),
    ]

    operations = [
        migrations.AlterField(
            model_name='client',
            name='emailId',
            field=models.EmailField(blank=True, max_length=254),
        ),
    ]