# Generated by Django 3.1.6 on 2021-07-24 08:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0004_auto_20210723_1502'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='slug',
            field=models.SlugField(blank=True, null=True, verbose_name='slug'),
        ),
        migrations.AlterField(
            model_name='profile',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='profile', verbose_name='الصورة الشخصية'),
        ),
    ]
