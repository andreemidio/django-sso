# Generated by Django 4.1.2 on 2023-02-02 20:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sso_gateway', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='authenticationrequest',
            name='used',
            field=models.BooleanField(default=False, verbose_name='Are used in external sso service'),
        ),
    ]