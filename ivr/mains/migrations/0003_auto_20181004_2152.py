# Generated by Django 2.1.1 on 2018-10-04 13:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mains', '0002_auto_20181004_2148'),
    ]

    operations = [
        migrations.AlterField(
            model_name='phonelist',
            name='star',
            field=models.CharField(default='普通', max_length=20),
        ),
    ]