# Generated by Django 4.1 on 2022-09-21 11:56

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0010_remove_profile_gallery_remove_profile_pricing_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='profilemodel',
            name='profile_link',
        ),
        migrations.DeleteModel(
            name='LinkModel',
        ),
    ]