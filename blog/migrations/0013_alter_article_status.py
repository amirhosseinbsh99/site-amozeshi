# Generated by Django 5.1.6 on 2025-03-27 12:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0012_article_image_alter_article_status'),
    ]

    operations = [
        migrations.AlterField(
            model_name='article',
            name='status',
            field=models.CharField(choices=[('archived', 'Archived'), ('published', 'Published'), ('draft', 'Draft')], default=None, max_length=20, null=True),
        ),
    ]
