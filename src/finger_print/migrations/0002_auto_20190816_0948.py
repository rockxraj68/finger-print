# Generated by Django 2.2.4 on 2019-08-16 09:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('finger_print', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='person',
            name='credentials',
            field=models.TextField(db_index=True, max_length=255, verbose_name='Credentials'),
        ),
    ]
