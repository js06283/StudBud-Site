# Generated by Django 3.1.4 on 2021-01-26 05:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('study', '0005_auto_20210125_1354'),
    ]

    operations = [
        migrations.AlterField(
            model_name='student',
            name='discovery',
            field=models.CharField(choices=[('class', 'Class'), ('discord', 'Discord'), ('facebook', 'Facebook'), ('friend', 'Friend'), ('groupme', 'GroupMe'), ('instagram', 'Instagram'), ('slack', 'Slack'), ('snapchat', 'Snapchat'), ('student_council', 'Student Council'), ('other', 'Other')], max_length=255),
        ),
    ]