# Generated by Django 4.0.4 on 2022-07-19 07:46

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('sportshub', '0005_alter_order_customer'),
    ]

    operations = [
        migrations.RenameField(
            model_name='order',
            old_name='customer',
            new_name='customer1',
        ),
    ]