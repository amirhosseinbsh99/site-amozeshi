# Generated by Django 5.1.6 on 2025-03-14 13:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0004_rename_post_course_alter_article_status'),
    ]

    operations = [
        migrations.AddField(
            model_name='course',
            name='teacher',
            field=models.CharField(default='nasri', max_length=150),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='article',
            name='status',
            field=models.CharField(choices=[('draft', 'Draft'), ('published', 'Published'), ('archived', 'Archived')], default=None, max_length=20, null=True),
        ),
    ]
