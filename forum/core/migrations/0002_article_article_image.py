# Generated by Django 2.2.6 on 2019-10-23 06:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='article',
            name='article_image',
            field=models.ImageField(default=1, upload_to=''),
            preserve_default=False,
        ),
    ]
