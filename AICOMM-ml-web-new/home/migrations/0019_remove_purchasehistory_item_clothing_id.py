# Generated by Django 5.0 on 2024-05-09 08:44

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0018_category_remove_product_clothing_id_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='purchasehistory',
            name='item_clothing_id',
        ),
    ]
