# Generated by Django 2.2.5 on 2021-07-10 00:53

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('flashCards', '0002_auto_20210709_1913'),
    ]

    operations = [
        migrations.RenameField(
            model_name='carddata',
            old_name='cards',
            new_name='deck',
        ),
    ]
