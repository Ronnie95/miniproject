# Generated by Django 4.2.2 on 2023-07-05 18:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0003_alter_movie_options_rename_name_movie_title'),
    ]

    operations = [
        migrations.RenameField(
            model_name='director',
            old_name='Movie',
            new_name='movie',
        ),
        migrations.RemoveField(
            model_name='director',
            name='hometown',
        ),
        migrations.AlterField(
            model_name='director',
            name='img',
            field=models.CharField(max_length=5000),
        ),
    ]
