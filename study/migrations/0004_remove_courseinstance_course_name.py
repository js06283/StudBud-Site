# Generated by Django 3.1.4 on 2020-12-30 23:23

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('study', '0003_courseinstance_course_name'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='courseinstance',
            name='course_name',
        ),
    ]