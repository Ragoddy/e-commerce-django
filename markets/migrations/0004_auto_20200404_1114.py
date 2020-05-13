# Generated by Django 3.0.5 on 2020-04-04 16:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('markets', '0003_auto_20200401_2314'),
    ]

    operations = [
        migrations.AddField(
            model_name='market',
            name='code',
            field=models.CharField(max_length=20, null=True, unique=True),
        ),
        migrations.AlterField(
            model_name='category',
            name='code',
            field=models.CharField(max_length=20, null=True, unique=True),
        ),
    ]
