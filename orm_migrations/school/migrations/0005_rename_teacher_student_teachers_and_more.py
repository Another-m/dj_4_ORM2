# Generated by Django 4.0.4 on 2022-05-25 14:11

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('school', '0004_teacherstudent'),
    ]

    operations = [
        migrations.RenameField(
            model_name='student',
            old_name='teacher',
            new_name='teachers',
        ),
        migrations.DeleteModel(
            name='TeacherStudent',
        ),
    ]
