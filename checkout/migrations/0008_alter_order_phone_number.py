# Generated by Django 3.2 on 2021-04-29 13:16

from django.db import migrations
import phone_field.models


class Migration(migrations.Migration):

    dependencies = [
        ('checkout', '0007_alter_order_phone_number'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='phone_number',
            field=phone_field.models.PhoneField(blank=True, help_text='Contact phone number', max_length=31),
        ),
    ]
