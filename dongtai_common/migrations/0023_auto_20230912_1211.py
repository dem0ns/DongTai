# Generated by Django 3.2.20 on 2023-09-12 12:11

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("dongtai_common", "0022_iastproject_token"),
    ]

    operations = [
        migrations.AddField(
            model_name="iastagentrequestchainstopographvec",
            name="expandable",
            field=models.BooleanField(default=False),
        ),
    ]
