# Generated by Django 4.2.5 on 2023-09-10 16:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sea', '0010_backgroundjob_celery_job_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='backgroundjob',
            name='celery_job_id',
            field=models.CharField(null=True),
        ),
    ]
