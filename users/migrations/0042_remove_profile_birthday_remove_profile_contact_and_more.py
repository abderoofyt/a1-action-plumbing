# Generated by Django 4.1 on 2022-10-09 19:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0041_alter_navbar_category'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='profile',
            name='birthday',
        ),
        migrations.RemoveField(
            model_name='profile',
            name='contact',
        ),
        migrations.RemoveField(
            model_name='profile',
            name='contact_details',
        ),
        migrations.RemoveField(
            model_name='profile',
            name='gallerys',
        ),
        migrations.RemoveField(
            model_name='profile',
            name='gallerys_details',
        ),
        migrations.RemoveField(
            model_name='profile',
            name='gender',
        ),
        migrations.RemoveField(
            model_name='profile',
            name='if_contact',
        ),
        migrations.RemoveField(
            model_name='profile',
            name='if_gallerys',
        ),
        migrations.RemoveField(
            model_name='profile',
            name='if_ourteam',
        ),
        migrations.RemoveField(
            model_name='profile',
            name='if_pricings',
        ),
        migrations.RemoveField(
            model_name='profile',
            name='if_services',
        ),
        migrations.RemoveField(
            model_name='profile',
            name='if_testimonial',
        ),
        migrations.RemoveField(
            model_name='profile',
            name='if_who_we_are',
        ),
        migrations.RemoveField(
            model_name='profile',
            name='ourteam',
        ),
        migrations.RemoveField(
            model_name='profile',
            name='ourteam_details',
        ),
        migrations.RemoveField(
            model_name='profile',
            name='phone',
        ),
        migrations.RemoveField(
            model_name='profile',
            name='pricings',
        ),
        migrations.RemoveField(
            model_name='profile',
            name='pricings_details',
        ),
        migrations.RemoveField(
            model_name='profile',
            name='services',
        ),
        migrations.RemoveField(
            model_name='profile',
            name='services_details',
        ),
        migrations.RemoveField(
            model_name='profile',
            name='testimonial',
        ),
        migrations.RemoveField(
            model_name='profile',
            name='testimonial_details',
        ),
        migrations.RemoveField(
            model_name='profile',
            name='who_we_are',
        ),
        migrations.RemoveField(
            model_name='profile',
            name='who_we_are_details',
        ),
        migrations.AlterField(
            model_name='navbar',
            name='category',
            field=models.TextField(blank=True, choices=[('pricing', 'Pricing'), ('services', 'services'), ('portfolio', 'gallery'), ('about', 'about'), ('team', 'team'), ('contact', 'contact')], null=True),
        ),
    ]
