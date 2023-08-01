# Generated by Django 3.2.5 on 2022-02-16 07:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ratinghome', '0007_auto_20220215_1935'),
    ]

    operations = [
        migrations.AddField(
            model_name='rateinfo',
            name='genre_bin',
            field=models.JSONField(default=[]),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='rateinfo',
            name='params',
            field=models.JSONField(default=[]),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='rateinfo',
            name='words_bin',
            field=models.JSONField(default=[]),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='rateinfo',
            name='pName',
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name='rateinfo',
            name='tags',
            field=models.JSONField(),
        ),
    ]