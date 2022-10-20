# Generated by Django 4.1 on 2022-09-14 12:50

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0009_remove_profile_services_service_user'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='profile',
            name='gallery',
        ),
        migrations.RemoveField(
            model_name='profile',
            name='pricing',
        ),
        migrations.RemoveField(
            model_name='profile',
            name='testimonials',
        ),
        migrations.AddField(
            model_name='gallery',
            name='user',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='users.profile'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='pricing',
            name='user',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='users.profile'),
            preserve_default=False,
        ),
    ]