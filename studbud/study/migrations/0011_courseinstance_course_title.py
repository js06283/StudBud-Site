# Generated by Django 3.2 on 2021-01-19 04:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('study', '0010_remove_student_course1'),
    ]

    operations = [
        migrations.AddField(
            model_name='courseinstance',
            name='course_title',
            field=models.CharField(default='', max_length=50),
        ),
    ]