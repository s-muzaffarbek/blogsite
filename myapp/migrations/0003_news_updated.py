# Generated by Django 4.0.3 on 2022-04-20 05:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0002_alter_category_options_alter_news_options'),
    ]

    operations = [
        migrations.AddField(
            model_name='news',
            name='updated',
            field=models.DateTimeField(auto_now=True),
        ),
    ]
