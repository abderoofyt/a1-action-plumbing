# Generated by Django 4.0.1 on 2022-11-03 12:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('styling', '0012_rename_nav_color_nav_bg_color_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='header',
            old_name='header_color_hover',
            new_name='header_hover_color',
        ),
        migrations.AddField(
            model_name='header',
            name='text_color',
            field=models.CharField(blank=True, max_length=20, null=True),
        ),
        migrations.AddField(
            model_name='header',
            name='text_hover_color',
            field=models.CharField(blank=True, max_length=20, null=True),
        ),
    ]
