# Generated by Django 5.0.4 on 2024-04-27 07:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tutor_app', '0003_remove_tutor_user_tutor_password_tutor_username'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tutor',
            name='username',
            field=models.CharField(max_length=150),
        ),
    ]