# Generated by Django 3.2 on 2021-04-29 13:15

from django.db import migrations
import phone_field.models


class Migration(migrations.Migration):

    dependencies = [
        ('checkout', '0006_auto_20210429_0037'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='phone_number',
            field=phone_field.models.PhoneField(blank=True, max_length=31),
        ),
    ]
