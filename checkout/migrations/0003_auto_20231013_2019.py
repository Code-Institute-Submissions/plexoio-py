# Generated by Django 3.2.20 on 2023-10-13 20:19

from django.db import migrations, models
import django.utils.timezone
import django_countries.fields


class Migration(migrations.Migration):

    dependencies = [
        ('checkout', '0002_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='order',
            name='original_bag',
        ),
        migrations.AddField(
            model_name='order',
            name='country',
            field=django_countries.fields.CountryField(max_length=2),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='order',
            name='stripe_pid',
            field=models.CharField(default='', max_length=254),
        ),
    ]
