# Generated by Django 4.1 on 2022-10-20 18:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0057_alter_order_amount'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='order',
            name='saving',
        ),
        migrations.AddField(
            model_name='profile',
            name='temp',
            field=models.TextField(choices=[('Green', 'Green'), ('Red', 'red')], default=1),
            preserve_default=False,
        ),
    ]