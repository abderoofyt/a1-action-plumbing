# Generated by Django 4.0.1 on 2022-10-27 14:48

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Filter',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=10)),
            ],
        ),
        migrations.CreateModel(
            name='Icon',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('icon', models.CharField(max_length=30)),
                ('icons', models.CharField(max_length=30)),
                ('fav', models.CharField(max_length=30)),
                ('shortcut', models.CharField(max_length=30)),
            ],
        ),
        migrations.CreateModel(
            name='Navbar',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('category', models.TextField(blank=True, choices=[('pricing', 'Pricing'), ('services', 'services'), ('services2', 'services2'), ('portfolio', 'gallery'), ('portfolio2', 'gallery2'), ('about', 'about'), ('team', 'team'), ('testimonial', 'testimonial'), ('contact', 'contact'), ('counter', 'counter')], null=True)),
                ('nav', models.CharField(blank=True, max_length=30, null=True)),
                ('details', models.CharField(blank=True, max_length=300, null=True)),
                ('photo', models.ImageField(blank=True, null=True, upload_to='photo/')),
                ('background_color', models.BooleanField()),
                ('background_photo', models.ImageField(blank=True, null=True, upload_to='photo/')),
            ],
        ),
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(blank=True, max_length=20, null=True)),
                ('name', models.CharField(blank=True, max_length=20, null=True)),
                ('price', models.CharField(blank=True, max_length=20, null=True)),
                ('payment', models.CharField(blank=True, max_length=20, null=True)),
                ('item_amount', models.IntegerField(blank=True, null=True)),
                ('item_quantity', models.CharField(blank=True, max_length=10, null=True)),
                ('item_name', models.CharField(blank=True, max_length=30, null=True)),
                ('amount', models.IntegerField(blank=True, default=1, null=True)),
                ('contact_info', models.CharField(blank=True, max_length=30, null=True)),
                ('message', models.CharField(blank=True, max_length=30, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('slug', models.SlugField(max_length=200)),
                ('motto', models.CharField(blank=True, max_length=100, null=True)),
                ('button', models.CharField(blank=True, max_length=30, null=True)),
                ('destination', models.CharField(blank=True, max_length=30, null=True)),
                ('year', models.IntegerField(blank=True, null=True)),
                ('logo', models.ImageField(blank=True, null=True, upload_to='logo/')),
                ('favicon', models.ImageField(blank=True, null=True, upload_to='logo/')),
                ('avatar', models.ImageField(blank=True, null=True, upload_to='avatars/')),
                ('address', models.CharField(blank=True, max_length=255, null=True)),
                ('number', models.CharField(blank=True, max_length=32, null=True)),
                ('city', models.CharField(blank=True, max_length=50, null=True)),
                ('zip', models.CharField(blank=True, max_length=30, null=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='profile', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'Profile',
                'verbose_name_plural': 'Profiles',
            },
        ),
        migrations.CreateModel(
            name='Testimonial',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nav', models.CharField(blank=True, max_length=30, null=True)),
                ('person', models.CharField(max_length=30)),
                ('quote', models.CharField(max_length=100)),
                ('photo', models.ImageField(blank=True, null=True, upload_to='photo/')),
                ('title', models.CharField(blank=True, max_length=30, null=True)),
                ('navbar', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='users.navbar')),
            ],
        ),
        migrations.CreateModel(
            name='Social',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('link', models.CharField(blank=True, max_length=300, null=True)),
                ('icon', models.CharField(blank=True, max_length=30, null=True)),
                ('user', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='users.profile')),
            ],
        ),
        migrations.CreateModel(
            name='Service',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nav', models.CharField(blank=True, max_length=30, null=True)),
                ('services', models.CharField(blank=True, max_length=30, null=True)),
                ('details', models.CharField(blank=True, max_length=300, null=True)),
                ('icon', models.CharField(blank=True, max_length=30, null=True)),
                ('navbar', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='users.navbar')),
            ],
        ),
        migrations.CreateModel(
            name='Pricing',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nav', models.CharField(blank=True, max_length=30, null=True)),
                ('title', models.CharField(blank=True, max_length=20, null=True)),
                ('features', models.BooleanField()),
                ('name', models.CharField(blank=True, max_length=20, null=True)),
                ('featured', models.BooleanField()),
                ('price', models.CharField(blank=True, max_length=20, null=True)),
                ('saving', models.CharField(blank=True, max_length=20, null=True)),
                ('payment', models.CharField(blank=True, max_length=20, null=True)),
                ('item_amount', models.IntegerField(blank=True, null=True)),
                ('item_quantity', models.CharField(blank=True, max_length=10, null=True)),
                ('item_name', models.CharField(blank=True, max_length=30, null=True)),
                ('navbar', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='users.navbar')),
            ],
        ),
        migrations.AddField(
            model_name='navbar',
            name='user',
            field=models.ForeignKey(blank=True, on_delete=django.db.models.deletion.CASCADE, to='users.profile'),
        ),
        migrations.CreateModel(
            name='Gallery',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nav', models.CharField(blank=True, max_length=30, null=True)),
                ('alt', models.CharField(max_length=30)),
                ('photo', models.ImageField(blank=True, null=True, upload_to='photo/')),
                ('filter', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='users.filter')),
                ('navbar', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='users.navbar')),
            ],
        ),
        migrations.CreateModel(
            name='Friend_Request',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('from_user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='from_user', to=settings.AUTH_USER_MODEL)),
                ('to_user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='to_user', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Counter',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nav', models.CharField(blank=True, max_length=30, null=True)),
                ('name', models.CharField(max_length=30)),
                ('number', models.IntegerField()),
                ('navbar', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='users.navbar')),
            ],
        ),
    ]