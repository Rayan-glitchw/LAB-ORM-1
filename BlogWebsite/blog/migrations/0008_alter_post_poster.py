# Generated by Django 5.0.2 on 2024-03-18 02:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0007_alter_post_poster'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='poster',
            field=models.ImageField(default='images/bg-blogger.jpeg', upload_to='images/'),
        ),
    ]
