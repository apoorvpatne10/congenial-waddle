# Generated by Django 3.0 on 2019-12-15 16:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0005_auto_20191215_1513'),
    ]

    operations = [
        migrations.AlterField(
            model_name='mymodel',
            name='file_name',
            field=models.CharField(default='temp', max_length=250),
        ),
    ]