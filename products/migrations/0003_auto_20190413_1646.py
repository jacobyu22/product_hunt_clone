# Generated by Django 2.2 on 2019-04-13 16:46

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0002_auto_20190413_1643'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='product_discoverer',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]
