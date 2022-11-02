# Generated by Django 4.0.1 on 2022-11-02 04:29

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0007_navbar_order'),
    ]

    operations = [
        migrations.RenameField(
            model_name='about',
            old_name='title',
            new_name='background',
        ),
        migrations.RenameField(
            model_name='about',
            old_name='photo',
            new_name='background_image',
        ),
        migrations.RemoveField(
            model_name='about',
            name='details',
        ),
        migrations.RemoveField(
            model_name='about',
            name='icon',
        ),
        migrations.RemoveField(
            model_name='about',
            name='nav',
        ),
        migrations.RemoveField(
            model_name='about',
            name='navbar',
        ),
    ]