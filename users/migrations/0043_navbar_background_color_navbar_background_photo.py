# Generated by Django 4.1 on 2022-10-09 20:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0042_remove_profile_birthday_remove_profile_contact_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='navbar',
            name='background_color',
            field=models.BooleanField(default=False),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='navbar',
            name='background_photo',
            field=models.ImageField(blank=True, null=True, upload_to='photo/'),
        ),
    ]