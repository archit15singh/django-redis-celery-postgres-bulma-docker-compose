# Generated by Django 4.2.5 on 2023-09-10 14:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sea', '0008_alter_backgroundjob_created_at_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='backgroundjob',
            name='status',
            field=models.CharField(choices=[('running', 'Running'), ('done', 'Done'), ('error', 'Error')], max_length=10),
        ),
    ]
