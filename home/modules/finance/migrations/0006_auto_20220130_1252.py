# Generated by Django 3.2.11 on 2022-01-30 12:52

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('finance', '0005_auto_20220130_1247'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='debtwallet',
            name='user',
        ),
        migrations.DeleteModel(
            name='Debt',
        ),
        migrations.DeleteModel(
            name='DebtWallet',
        ),
    ]
