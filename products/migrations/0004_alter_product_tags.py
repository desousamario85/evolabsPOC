# Generated by Django 3.2 on 2023-04-18 20:50

from django.db import migrations
import multiselectfield.db.fields


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0003_auto_20230418_2044'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='tags',
            field=multiselectfield.db.fields.MultiSelectField(choices=[('Power BI', 'PowerBI'), ('Power Apps', 'PowerApps'), ('Power Apps', 'PowerAutomate'), ('Power Virtual Agents', 'PowerVA'), ('Android', 'Android'), ('iOS', 'iOS'), ('JavaScript', 'Javascript'), ('React', 'React'), ('Django', 'Django'), ('DocuSign', 'DocuSign'), ('Stripe', 'Stripe')], max_length=50),
        ),
    ]