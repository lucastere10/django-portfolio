# Generated by Django 4.2 on 2023-05-23 20:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user_app', '0004_alter_profile_education_alter_profile_languages_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='birthdate',
            field=models.DateTimeField(help_text='your birthday :)', null=True),
        ),
        migrations.AddField(
            model_name='profile',
            name='gender',
            field=models.CharField(choices=[('M', 'Male'), ('F', 'Female')], default='M', max_length=1),
        ),
        migrations.AlterField(
            model_name='profile',
            name='thumbnail',
            field=models.ImageField(blank=True, default='UserProfile.png', null=True, upload_to='users/thumb'),
        ),
    ]