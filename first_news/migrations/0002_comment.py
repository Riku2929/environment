# Generated by Django 2.1.15 on 2021-11-03 17:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('first_news', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20, verbose_name='名前')),
                ('text', models.TextField(verbose_name='本文')),
            ],
        ),
    ]
