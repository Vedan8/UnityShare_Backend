# Generated by Django 5.0.1 on 2024-01-27 14:39

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('category', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='yourmodel',
            old_name='name',
            new_name='category',
        ),
    ]