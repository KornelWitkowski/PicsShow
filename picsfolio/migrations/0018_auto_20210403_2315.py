# Generated by Django 3.1.7 on 2021-04-03 21:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('picsfolio', '0017_usercatalog_imageslist'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='usercatalog',
            name='imagesList',
        ),
        migrations.AddField(
            model_name='userimage',
            name='catalog',
            field=models.CharField(default='All', max_length=200),
        ),
    ]
