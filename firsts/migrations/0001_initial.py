# Generated by Django 4.0.1 on 2022-11-02 20:03

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('users', '0010_alter_navbar_category'),
    ]

    operations = [
        migrations.CreateModel(
            name='Navbar',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('category', models.TextField(blank=True, choices=[('pricing', 'Pricing'), ('services', 'services'), ('services2', 'services2'), ('portfolio', 'gallery'), ('portfolio2', 'gallery2'), ('About', 'About'), ('team', 'team'), ('testimonial', 'testimonial'), ('contact', 'contact'), ('counter', 'counter')], null=True)),
                ('order', models.IntegerField(blank=True, null=True, unique=True)),
                ('nav', models.CharField(blank=True, max_length=30, null=True)),
                ('details', models.CharField(blank=True, max_length=300, null=True)),
                ('photo', models.ImageField(blank=True, null=True, upload_to='photo/')),
                ('background', models.CharField(blank=True, max_length=30, null=True)),
                ('background_image', models.ImageField(blank=True, null=True, upload_to='photo/')),
                ('user', models.ForeignKey(blank=True, on_delete=django.db.models.deletion.CASCADE, to='users.profile')),
            ],
        ),
    ]
