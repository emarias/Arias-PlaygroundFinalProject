# Generated by Django 5.0.3 on 2024-03-15 03:20

import ckeditor.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('vehiculos', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='autos',
            name='descripcion',
            field=ckeditor.fields.RichTextField(null=True),
        ),
    ]
