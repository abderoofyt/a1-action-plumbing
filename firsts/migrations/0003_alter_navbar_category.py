# Generated by Django 4.0.1 on 2022-11-04 07:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('firsts', '0002_alter_navbar_category'),
    ]

    operations = [
        migrations.AlterField(
            model_name='navbar',
            name='category',
            field=models.TextField(blank=True, choices=[('pricing', 'pricing'), ('services', 'services'), ('portfolio', 'gallery'), ('About', 'About'), ('team', 'team'), ('testimonial', 'testimonial'), ('contact', 'contact'), ('counter', 'counter')], null=True),
        ),
    ]
