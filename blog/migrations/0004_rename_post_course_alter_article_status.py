# Generated by Django 5.1.6 on 2025-03-09 11:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0003_alter_article_status'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Post',
            new_name='Course',
        ),
        migrations.AlterField(
            model_name='article',
            name='status',
            field=models.CharField(choices=[('archived', 'Archived'), ('draft', 'Draft'), ('published', 'Published')], default=None, max_length=20, null=True),
        ),
    ]
