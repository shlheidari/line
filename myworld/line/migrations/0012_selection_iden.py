# Generated by Django 4.1.1 on 2023-01-30 13:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("line", "0011_rename_choice_en_selection_choice_and_more"),
    ]

    operations = [
        migrations.AddField(
            model_name="selection",
            name="iden",
            field=models.CharField(default=1, max_length=255),
            preserve_default=False,
        ),
    ]
