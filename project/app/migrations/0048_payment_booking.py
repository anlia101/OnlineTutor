# Generated by Django 5.0.1 on 2024-03-20 09:21

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0047_remove_booking1_payment'),
    ]

    operations = [
        migrations.AddField(
            model_name='payment',
            name='booking',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='app.booking1'),
        ),
    ]