# Generated by Django 2.2 on 2019-04-13 20:49

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0003_auto_20190413_1646'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='product_discoverer',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]