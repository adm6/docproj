# Generated by Django 3.1.7 on 2021-03-08 10:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('doctor', '0007_consultation'),
    ]

    operations = [
        migrations.CreateModel(
            name='Pedometer',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('content', models.TextField()),
                ('image', models.ImageField(default='def_img_for_articles.jpg', upload_to='static/doctor')),
            ],
        ),
    ]