# Generated by Django 3.2.15 on 2022-10-06 04:05

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('booking', '0011_book_phone_no'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='services',
            name='price_2',
        ),
        migrations.RemoveField(
            model_name='services',
            name='price_3',
        ),
        migrations.RemoveField(
            model_name='services',
            name='price_4',
        ),
        migrations.RemoveField(
            model_name='services',
            name='price_5',
        ),
        migrations.RemoveField(
            model_name='services',
            name='service_2',
        ),
        migrations.RemoveField(
            model_name='services',
            name='service_3',
        ),
        migrations.RemoveField(
            model_name='services',
            name='service_4',
        ),
        migrations.RemoveField(
            model_name='services',
            name='service_5',
        ),
    ]
