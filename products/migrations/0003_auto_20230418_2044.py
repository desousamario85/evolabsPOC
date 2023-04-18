# Generated by Django 3.2 on 2023-04-18 20:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0002_auto_20230418_2043'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='license',
            field=models.CharField(choices=[('Device', 'Device'), ('User', 'User')], max_length=50),
        ),
        migrations.AlterField(
            model_name='product',
            name='tags',
            field=models.CharField(choices=[('Power BI', 'PowerBI'), ('Power Apps', 'PowerApps'), ('Power Apps', 'PowerAutomate'), ('Power Virtual Agents', 'PowerVA'), ('Android', 'Android'), ('iOS', 'iOS'), ('JavaScript', 'Javascript'), ('React', 'React'), ('Django', 'Django'), ('DocuSign', 'DocuSign'), ('Stripe', 'Stripe')], max_length=50),
        ),
    ]
