# Generated by Django 4.1.5 on 2023-02-14 13:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cartanother', '0005_ordernew_order_complete'),
    ]

    operations = [
        migrations.AddField(
            model_name='ordernew',
            name='order_final_complete',
            field=models.BooleanField(default=False),
        ),
    ]
