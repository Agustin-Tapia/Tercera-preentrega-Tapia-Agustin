# Generated by Django 4.1.7 on 2023-03-19 18:50

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('casa', '0003_rename_silla_mesas_rename_sillon_sillas_and_more'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Mesas',
            new_name='Mesa',
        ),
        migrations.RenameModel(
            old_name='Sillas',
            new_name='Silla',
        ),
        migrations.RenameModel(
            old_name='Sillones',
            new_name='Sillon',
        ),
    ]
