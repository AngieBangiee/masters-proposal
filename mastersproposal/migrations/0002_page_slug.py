# Generated by Django 4.0.4 on 2022-04-25 04:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mastersproposal', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='page',
            name='slug',
            field=models.SlugField(max_length=255, null=True, unique=True),
        ),
    ]
