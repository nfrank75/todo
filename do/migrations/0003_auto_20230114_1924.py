# Generated by Django 3.2.7 on 2023-01-14 19:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('do', '0002_auto_20230114_1019'),
    ]

    operations = [
        migrations.AlterField(
            model_name='todo',
            name='File',
            field=models.FileField(blank=True, null=True, upload_to='Todo', verbose_name='File'),
        ),
        migrations.AlterField(
            model_name='todo',
            name='complete',
            field=models.BooleanField(default=False, verbose_name='Complete'),
        ),
        migrations.AlterField(
            model_name='todo',
            name='name',
            field=models.CharField(max_length=150, verbose_name='Title'),
        ),
    ]
