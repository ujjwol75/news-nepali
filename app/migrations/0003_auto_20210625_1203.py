# Generated by Django 3.2 on 2021-06-25 06:18

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0002_comments_news'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='category',
            options={'verbose_name_plural': 'Categories'},
        ),
        migrations.AlterModelOptions(
            name='comments',
            options={'verbose_name_plural': 'Comments'},
        ),
        migrations.AlterModelOptions(
            name='news',
            options={'verbose_name_plural': 'News'},
        ),
    ]
