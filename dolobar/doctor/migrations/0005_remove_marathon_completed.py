# Generated by Django 3.1.7 on 2021-03-07 19:42

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('doctor', '0004_auto_20210307_1658'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='marathon',
            name='completed',
        ),
    ]