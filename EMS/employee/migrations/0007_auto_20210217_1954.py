# Generated by Django 3.1.6 on 2021-02-17 19:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('employee', '0006_salary'),
    ]

    operations = [
        migrations.AlterField(
            model_name='salary',
            name='salary',
            field=models.IntegerField(),
        ),
    ]
