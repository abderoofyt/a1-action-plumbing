# Generated by Django 4.1 on 2022-10-10 07:08

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0043_navbar_background_color_navbar_background_photo'),
    ]

    operations = [
        migrations.AlterField(
            model_name='navbar',
            name='category',
            field=models.TextField(blank=True, choices=[('pricing', 'Pricing'), ('services', 'services'), ('services2', 'services2'), ('portfolio', 'gallery'), ('portfolio2', 'gallery2'), ('about', 'about'), ('team', 'team'), ('contact', 'contact')], null=True),
        ),
        migrations.AlterField(
            model_name='service',
            name='user',
            field=models.ForeignKey(blank=True, on_delete=django.db.models.deletion.CASCADE, to='users.navbar'),
        ),
    ]