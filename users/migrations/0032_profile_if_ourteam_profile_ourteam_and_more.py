# Generated by Django 4.1 on 2022-10-06 17:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0031_profile_if_gallerys_profile_if_pricings_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='if_ourteam',
            field=models.BooleanField(default=True),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='profile',
            name='ourteam',
            field=models.CharField(blank=True, max_length=30, null=True),
        ),
        migrations.AddField(
            model_name='profile',
            name='ourteam_details',
            field=models.CharField(blank=True, max_length=300, null=True),
        ),
    ]