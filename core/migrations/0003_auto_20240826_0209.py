# Generated by Django 3.2.25 on 2024-08-26 02:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0002_deliverylocation'),
    ]

    operations = [
        migrations.AlterField(
            model_name='deliverylocation',
            name='latitude',
            field=models.FloatField(db_index=True),
        ),
        migrations.AlterField(
            model_name='deliverylocation',
            name='longitude',
            field=models.FloatField(db_index=True),
        ),
        migrations.AlterField(
            model_name='user',
            name='email',
            field=models.EmailField(db_index=True, max_length=255, unique=True),
        ),
        migrations.AlterField(
            model_name='user',
            name='username',
            field=models.CharField(db_index=True, max_length=255),
        ),
    ]