# Generated by Django 3.2.11 on 2022-01-30 12:56

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('finance', '0007_debt_debtwallet'),
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