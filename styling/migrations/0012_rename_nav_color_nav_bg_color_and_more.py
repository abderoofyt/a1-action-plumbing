# Generated by Django 4.0.1 on 2022-11-03 11:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('styling', '0011_rename_footer_color_footer_bg_color_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='nav',
            old_name='nav_color',
            new_name='bg_color',
        ),
        migrations.RenameField(
            model_name='nav',
            old_name='nav_direction',
            new_name='color',
        ),
        migrations.RenameField(
            model_name='nav',
            old_name='nav_style',
            new_name='direction',
        ),
        migrations.AddField(
            model_name='nav',
            name='hover_bg_color',
            field=models.CharField(blank=True, max_length=20, null=True),
        ),
        migrations.AddField(
            model_name='nav',
            name='hover_color',
            field=models.CharField(blank=True, max_length=20, null=True),
        ),
        migrations.AddField(
            model_name='nav',
            name='style',
            field=models.CharField(blank=True, max_length=20, null=True),
        ),
    ]
