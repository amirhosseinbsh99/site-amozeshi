# Generated by Django 4.1.3 on 2025-02-12 11:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0006_myuser_token_send'),
    ]

    operations = [
        migrations.AddField(
            model_name='myuser',
            name='is_admin',
            field=models.BooleanField(default=False),
        ),
    ]
