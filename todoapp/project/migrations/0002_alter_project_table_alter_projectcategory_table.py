# Generated by Django 4.0.2 on 2022-02-24 07:58

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('project', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelTable(
            name='project',
            table='project',
        ),
        migrations.AlterModelTable(
            name='projectcategory',
            table='category',
        ),
    ]