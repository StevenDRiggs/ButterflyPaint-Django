# Generated by Django 2.2.4 on 2019-08-30 06:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bpaint_app', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='oilacryliccolor',
            name='color_image',
            field=models.ImageField(upload_to='images/'),
        ),
        migrations.AlterField(
            model_name='watercolorcolor',
            name='color_image',
            field=models.ImageField(upload_to='images/'),
        ),
    ]