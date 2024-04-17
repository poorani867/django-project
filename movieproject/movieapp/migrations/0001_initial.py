# Generated by Django 4.2.9 on 2024-02-18 08:06

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Movie',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('MovieName', models.CharField(max_length=50)),
                ('MovieDirector', models.CharField(max_length=50)),
                ('Language', models.CharField(max_length=50)),
                ('Budget', models.IntegerField()),
            ],
        ),
    ]
