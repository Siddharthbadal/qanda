# Generated by Django 3.2.9 on 2021-12-02 11:24

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('questions', '0003_question_post_like'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='question',
            name='post_like',
        ),
    ]
