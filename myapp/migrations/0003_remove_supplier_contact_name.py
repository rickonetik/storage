# Generated by Django 3.2 on 2023-07-21 02:24

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0002_auto_20230721_0217'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='supplier',
            name='contact_name',
        ),
    ]
