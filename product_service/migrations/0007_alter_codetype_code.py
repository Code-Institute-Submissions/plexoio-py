# Generated by Django 3.2.20 on 2023-09-04 15:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('product_service', '0006_alter_codetype_code'),
    ]

    operations = [
        migrations.AlterField(
            model_name='codetype',
            name='code',
            field=models.IntegerField(choices=[(0, 'HTML'), (1, 'CSS'), (2, 'JS'), (3, 'PY'), (4, 'MD')], unique=True),
        ),
    ]
