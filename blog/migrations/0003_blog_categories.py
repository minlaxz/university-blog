# Generated by Django 3.1.5 on 2021-01-12 10:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0002_auto_20210112_1634'),
    ]

    operations = [
        migrations.AddField(
            model_name='blog',
            name='categories',
            field=models.ManyToManyField(related_name='posts', to='blog.Category'),
        ),
    ]
