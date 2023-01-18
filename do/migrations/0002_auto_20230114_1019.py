# Generated by Django 3.2.7 on 2023-01-14 10:19

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('do', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='todo',
            name='todo',
        ),
        migrations.AddField(
            model_name='todo',
            name='File',
            field=models.FileField(blank=True, null=True, upload_to='Assignments', verbose_name='Add a file'),
        ),
        migrations.AddField(
            model_name='todo',
            name='complete',
            field=models.BooleanField(default=False, verbose_name='Is Complete ?'),
        ),
        migrations.AddField(
            model_name='todo',
            name='created_at',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='todo',
            name='description',
            field=models.CharField(blank=True, max_length=250, null=True, verbose_name='Description'),
        ),
        migrations.AddField(
            model_name='todo',
            name='name',
            field=models.CharField(default=django.utils.timezone.now, max_length=150, verbose_name='To Do Name'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='todo',
            name='updated_at',
            field=models.DateTimeField(auto_now_add=True, null=True),
        ),
    ]