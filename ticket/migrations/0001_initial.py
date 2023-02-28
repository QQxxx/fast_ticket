# Generated by Django 4.0.4 on 2023-02-28 09:41

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Model',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30)),
            ],
        ),
        migrations.CreateModel(
            name='Ticket',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=128)),
                ('year', models.PositiveIntegerField()),
                ('month', models.PositiveIntegerField()),
                ('version', models.CharField(max_length=128)),
                ('model', models.ManyToManyField(to='ticket.model')),
            ],
        ),
    ]
