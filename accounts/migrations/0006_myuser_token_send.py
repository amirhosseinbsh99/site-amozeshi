# Generated by Django 4.1.3 on 2023-02-13 11:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0005_alter_myuser_phone_number'),
    ]

    operations = [
        migrations.AddField(
            model_name='myuser',
            name='token_send',
            field=models.IntegerField(blank=True, null=True),
        ),
    ]
