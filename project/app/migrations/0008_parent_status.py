# Generated by Django 5.0.1 on 2024-01-25 04:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0007_teacher_status_select_tutor_delete_tutor'),
    ]

    operations = [
        migrations.AddField(
            model_name='parent',
            name='status',
            field=models.CharField(default='pending', max_length=20),
        ),
    ]
