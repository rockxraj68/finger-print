# Generated by Django 2.2.4 on 2019-08-16 09:24

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Person',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(db_index=True, max_length=255, verbose_name='Person Name')),
                ('bio_id', models.PositiveIntegerField(verbose_name='Biometric Id')),
                ('credentials', models.CharField(db_index=True, max_length=255, verbose_name='Credentials')),
                ('created_on', models.DateTimeField(auto_now_add=True, verbose_name='Created On')),
                ('updated_on', models.DateTimeField(auto_now=True, verbose_name='Updated On')),
            ],
        ),
    ]
