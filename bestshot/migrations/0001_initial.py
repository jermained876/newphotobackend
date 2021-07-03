# Generated by Django 3.1.7 on 2021-06-16 16:33

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Bestshot',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('asset_id', models.CharField(blank=True, max_length=400, null=True)),
                ('bytes', models.IntegerField(blank=True, default=0, null=True)),
                ('created_at', models.CharField(blank=True, max_length=250, null=True)),
                ('etag', models.CharField(blank=True, max_length=250, null=True)),
                ('format', models.CharField(blank=True, max_length=250, null=True)),
                ('height', models.IntegerField(blank=True, default=0, null=True)),
                ('original_filename', models.CharField(blank=True, max_length=250, null=True)),
                ('public_id', models.CharField(blank=True, max_length=250, null=True)),
                ('resource_type', models.CharField(blank=True, max_length=250, null=True)),
                ('secure_url', models.CharField(blank=True, max_length=250, null=True)),
                ('signature', models.CharField(blank=True, max_length=250, null=True)),
                ('url', models.CharField(blank=True, max_length=250, null=True)),
                ('width', models.IntegerField(blank=True, default=0, null=True)),
            ],
        ),
    ]
