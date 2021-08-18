# Generated by Django 3.2.6 on 2021-08-18 18:04

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import website.validators


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Organisation',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(help_text='Organisation Name', max_length=250)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Scholar',
            fields=[
                ('id', models.CharField(help_text='Scholar User id', max_length=20, primary_key=True, serialize=False, validators=[website.validators.scholar_id_validator])),
                ('name', models.CharField(blank=True, help_text='Scholar Name', max_length=100)),
                ('organisations', models.ManyToManyField(blank=True, to='website.Organisation')),
            ],
        ),
        migrations.CreateModel(
            name='Paper',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200)),
                ('url', models.URLField()),
                ('year', models.CharField(max_length=4, validators=[website.validators.year_validator])),
                ('citation', models.IntegerField()),
                ('author', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='website.scholar')),
            ],
        ),
    ]