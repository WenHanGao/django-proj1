# Generated by Django 3.1.4 on 2020-12-28 13:45

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='choice',
            old_name='choice_txt',
            new_name='choice_text',
        ),
    ]
