# Generated by Django 4.1.1 on 2022-12-23 12:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("line", "0003_members_pediatric"),
    ]

    operations = [
        migrations.CreateModel(
            name="Capacity",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("line", models.CharField(max_length=255)),
                ("unit", models.CharField(max_length=255)),
                ("hospital", models.CharField(max_length=255)),
                ("full", models.CharField(max_length=255)),
                ("remain", models.CharField(max_length=255)),
            ],
        ),
    ]