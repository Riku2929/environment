# Generated by Django 2.2.17 on 2021-11-04 07:57

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('first_news', '0006_auto_20211104_1301'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comment',
            name='article',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='first_news.Article', verbose_name='記事'),
        ),
    ]
