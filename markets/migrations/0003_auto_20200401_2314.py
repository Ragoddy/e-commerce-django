# Generated by Django 3.0.4 on 2020-04-02 04:14

from django.db import migrations, models
import markets.models


class Migration(migrations.Migration):

    dependencies = [
        ('markets', '0002_schedule'),
    ]

    operations = [
        migrations.AddField(
            model_name='market',
            name='creation_date',
            field=models.DateTimeField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='category',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to=markets.models.category_path),
        ),
        migrations.AlterField(
            model_name='product',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to=markets.models.product_path),
        ),
    ]
