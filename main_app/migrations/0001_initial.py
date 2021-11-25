# Generated by Django 3.2.9 on 2021-11-25 01:42

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Trip',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('type', models.CharField(choices=[('s', 'Street'), ('r', 'Road'), ('t', 'Track')], default='s', max_length=1)),
                ('distance', models.IntegerField()),
                ('description', models.TextField(max_length=500)),
                ('topspeed', models.IntegerField()),
            ],
        ),
    ]
