# Generated by Django 3.1.7 on 2021-04-04 21:59

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='FileType',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=250, null=True)),
                ('slug', models.SlugField(blank=True, max_length=250, null=True, unique=True)),
            ],
        ),
    ]
