# Generated by Django 3.1.7 on 2021-08-30 03:56

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('library', '0009_student_roll_no'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='issuedbook',
            name='branch',
        ),
    ]
