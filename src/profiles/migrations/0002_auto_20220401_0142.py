# Generated by Django 3.2.12 on 2022-03-31 23:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('profiles', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='profiles',
            old_name='member',
            new_name='author',
        ),
        migrations.AddField(
            model_name='profiles',
            name='job_title',
            field=models.CharField(default='coding', max_length=50),
        ),
    ]
