# Generated by Django 3.0.4 on 2020-04-11 11:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Doctor', '0005_appointment_treated'),
    ]

    operations = [
        migrations.AddField(
            model_name='appointment',
            name='remark',
            field=models.TextField(default=0),
            preserve_default=False,
        ),
    ]
