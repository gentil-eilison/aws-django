# Generated by Django 4.2.3 on 2023-07-13 13:45

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("core", "0001_initial"),
    ]

    operations = [
        migrations.CreateModel(
            name="CeleryCompletedTasks",
            fields=[
                ("id", models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name="ID")),
                ("message", models.CharField(max_length=100)),
                ("success", models.BooleanField()),
            ],
        ),
    ]
