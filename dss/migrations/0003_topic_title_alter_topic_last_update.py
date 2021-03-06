# Generated by Django 4.0.2 on 2022-02-20 13:16

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('dss', '0002_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='topic',
            name='title',
            field=models.CharField(default=django.utils.timezone.now, max_length=200),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='topic',
            name='last_update',
            field=models.DateTimeField(auto_now=True),
        ),
    ]
