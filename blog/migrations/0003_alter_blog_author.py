# Generated by Django 4.0 on 2022-01-29 09:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0002_alter_blog_author'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blog',
            name='author',
            field=models.CharField(max_length=50),
        ),
    ]