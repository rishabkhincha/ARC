# Generated by Django 2.0.1 on 2018-04-09 17:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0003_auto_20180222_1520'),
    ]

    operations = [
        migrations.AddField(
            model_name='courseslot',
            name='catalog',
            field=models.CharField(max_length=4, null=True),
        ),
        migrations.AddField(
            model_name='courseslot',
            name='course_title',
            field=models.CharField(max_length=40, null=True),
        ),
        migrations.AddField(
            model_name='courseslot',
            name='subject',
            field=models.CharField(max_length=5, null=True),
        ),
    ]
