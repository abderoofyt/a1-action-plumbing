# Generated by Django 4.1 on 2022-10-06 10:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0028_navbar'),
    ]

    operations = [
        migrations.AddField(
            model_name='navbar',
            name='details',
            field=models.CharField(blank=True, max_length=300, null=True),
        ),
    ]