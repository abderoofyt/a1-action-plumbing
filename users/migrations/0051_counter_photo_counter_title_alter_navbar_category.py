# Generated by Django 4.1 on 2022-10-10 17:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0050_rename_counters_counter'),
    ]

    operations = [
        migrations.AddField(
            model_name='counter',
            name='photo',
            field=models.ImageField(blank=True, null=True, upload_to='photo/'),
        ),
        migrations.AddField(
            model_name='counter',
            name='title',
            field=models.CharField(blank=True, max_length=30, null=True),
        ),
        migrations.AlterField(
            model_name='navbar',
            name='category',
            field=models.TextField(blank=True, choices=[('pricing', 'Pricing'), ('services', 'services'), ('services2', 'services2'), ('portfolio', 'gallery'), ('portfolio2', 'gallery2'), ('about', 'about'), ('team', 'team'), ('testimonial', 'testimonial'), ('contact', 'contact'), ('counter', 'counter')], null=True),
        ),
    ]
