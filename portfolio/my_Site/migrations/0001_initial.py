# Generated by Django 4.1.2 on 2022-10-16 11:45

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='MyWorks',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(blank=True, max_length=100, null=True)),
                ('description', models.TextField(blank=True, null=True)),
                ('image', models.ImageField(blank=True, null=True, upload_to='')),
                ('site_url', models.CharField(blank=True, default='#', max_length=100, null=True)),
                ('github_url', models.CharField(blank=True, default='#', max_length=100, null=True)),
            ],
        ),
    ]
