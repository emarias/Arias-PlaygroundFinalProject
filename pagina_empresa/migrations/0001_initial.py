# Generated by Django 5.0.3 on 2024-03-15 02:30

import ckeditor.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Empleado',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=30)),
                ('apellido', models.CharField(max_length=30)),
                ('edad', models.IntegerField()),
                ('sector', models.CharField(max_length=30)),
                ('sobre_mi', ckeditor.fields.RichTextField(null=True)),
            ],
        ),
    ]
