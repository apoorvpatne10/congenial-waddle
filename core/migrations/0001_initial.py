# Generated by Django 2.2.3 on 2019-12-15 11:03

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='MyModelPartOne',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('my_file', models.FileField(upload_to='media/')),
                ('encrypted_val', models.CharField(max_length=1000)),
            ],
        ),
    ]
