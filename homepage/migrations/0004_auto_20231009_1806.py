# Generated by Django 3.2.20 on 2023-10-09 18:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('homepage', '0003_auto_20231009_1745'),
    ]

    operations = [
        migrations.AddField(
            model_name='comment',
            name='instance',
            field=models.IntegerField(choices=[(0, 'Product'), (1, 'Service')], default=0),
        ),
        migrations.AddField(
            model_name='like',
            name='instance',
            field=models.IntegerField(choices=[(0, 'Product'), (1, 'Service')], default=1),
        ),
    ]
