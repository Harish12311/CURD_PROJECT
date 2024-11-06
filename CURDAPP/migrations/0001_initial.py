# Generated by Django 5.1.1 on 2024-10-08 11:22

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='CurdPro',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=50)),
                ('last_name', models.CharField(max_length=50)),
                ('email', models.EmailField(max_length=254)),
                ('mobile', models.BigIntegerField()),
                ('percentage', models.IntegerField()),
                ('year', models.IntegerField()),
                ('location', models.CharField(max_length=50)),
                ('college', models.CharField(max_length=50)),
                ('university', models.CharField(max_length=50)),
            ],
        ),
    ]
