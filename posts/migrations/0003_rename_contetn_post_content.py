# Generated by Django 4.2.1 on 2023-05-21 11:56

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0002_post_writer_alter_post_created_at_alter_post_image_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='post',
            old_name='contetn',
            new_name='content',
        ),
    ]
