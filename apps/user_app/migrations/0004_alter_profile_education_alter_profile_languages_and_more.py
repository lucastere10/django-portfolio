# Generated by Django 4.2 on 2023-05-23 13:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user_app', '0003_alter_profile_thumbnail'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='education',
            field=models.TextField(null=True),
        ),
        migrations.AlterField(
            model_name='profile',
            name='languages',
            field=models.TextField(null=True),
        ),
        migrations.AlterField(
            model_name='profile',
            name='skills',
            field=models.TextField(null=True),
        ),
    ]