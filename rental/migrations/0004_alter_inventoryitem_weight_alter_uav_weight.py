# Generated by Django 5.0.6 on 2024-06-05 19:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('rental', '0003_inventoryitem_remove_rental_user_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='inventoryitem',
            name='weight',
            field=models.DecimalField(decimal_places=2, max_digits=10),
        ),
        migrations.AlterField(
            model_name='uav',
            name='weight',
            field=models.DecimalField(decimal_places=2, max_digits=10),
        ),
    ]
