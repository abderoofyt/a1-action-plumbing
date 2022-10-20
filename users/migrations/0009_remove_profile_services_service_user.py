# Generated by Django 4.1 on 2022-09-14 12:44

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0008_remove_profile_icons_remove_profile_navbar_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='profile',
            name='services',
        ),
        migrations.AddField(
            model_name='service',
            name='user',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='users.profile'),
            preserve_default=False,
        ),
    ]