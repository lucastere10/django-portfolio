# Generated by Django 4.2 on 2023-05-22 22:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user_app', '0002_profile_name_profile_thumbnail'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='thumbnail',
            field=models.ImageField(default='UserProfile.png', null=True, upload_to='users/thumb'),
        ),
    ]