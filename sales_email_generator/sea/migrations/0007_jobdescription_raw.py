# Generated by Django 4.2.5 on 2023-09-10 13:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sea', '0006_email_type'),
    ]

    operations = [
        migrations.AddField(
            model_name='jobdescription',
            name='raw',
            field=models.CharField(default=None, max_length=255),
            preserve_default=False,
        ),
    ]
