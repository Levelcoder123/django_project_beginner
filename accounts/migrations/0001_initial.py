# Generated by Django 4.2.7 on 2023-12-05 08:34

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('banks', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Account',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('number', models.IntegerField()),
                ('type', models.CharField(max_length=15)),
                ('amount', models.IntegerField()),
                ('bank', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='banks.bank')),
            ],
        ),
    ]
