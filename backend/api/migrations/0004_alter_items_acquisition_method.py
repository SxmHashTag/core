# Generated by Django 5.2 on 2025-04-23 13:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0003_items_acquisition_date_items_acquisition_method'),
    ]

    operations = [
        migrations.AlterField(
            model_name='items',
            name='acquisition_method',
            field=models.CharField(choices=[('GrayKey', 'Graykey'), ('Cellebrite', 'Cellebrite'), ('Other', 'Other')], max_length=50),
        ),
    ]
