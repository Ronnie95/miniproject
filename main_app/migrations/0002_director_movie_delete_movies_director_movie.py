# Generated by Django 4.2.2 on 2023-07-04 12:15

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Director',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=150)),
                ('hometown', models.CharField(max_length=250)),
                ('age', models.CharField(max_length=250)),
                ('img', models.CharField(max_length=250)),
            ],
        ),
        migrations.CreateModel(
            name='Movie',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('img', models.CharField(max_length=250)),
            ],
            options={
                'ordering': ['name'],
            },
        ),
        migrations.DeleteModel(
            name='Movies',
        ),
        migrations.AddField(
            model_name='director',
            name='Movie',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='directors', to='main_app.movie'),
        ),
    ]