# Generated by Django 4.0.2 on 2022-02-25 07:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('project', '0003_project_created_at_project_project_status'),
    ]

    operations = [
        migrations.AddField(
            model_name='project',
            name='updated_at',
            field=models.DateTimeField(auto_now=True, null=True),
        ),
    ]