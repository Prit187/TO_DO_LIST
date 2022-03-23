# Generated by Django 4.0.2 on 2022-03-05 03:46

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Ticket',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ticket_name', models.CharField(max_length=100)),
                ('ticket_description', models.TextField()),
            ],
            options={
                'db_table': 'ticket',
            },
        ),
    ]
