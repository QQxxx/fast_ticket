# Generated by Django 4.0.4 on 2023-02-28 18:14

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ticket', '0006_alter_ticket_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ticket',
            name='date',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2023, 2, 28, 18, 14, 52, 9530)),
        ),
    ]
