# Generated by Django 4.2.7 on 2023-11-29 12:12

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='account',
            old_name='amount',
            new_name='account_amount',
        ),
    ]
