# Generated by Django 5.0.6 on 2024-06-20 05:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("todos", "0004_person_id_alter_person_dni"),
    ]

    operations = [
        migrations.AlterField(
            model_name="person",
            name="dni",
            field=models.CharField(max_length=9, unique=True),
        ),
    ]
