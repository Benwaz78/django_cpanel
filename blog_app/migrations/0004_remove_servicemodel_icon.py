# Generated by Django 4.1.7 on 2023-03-16 08:46

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog_app', '0003_alter_post_pst_image_alter_post_pst_title'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='servicemodel',
            name='icon',
        ),
    ]