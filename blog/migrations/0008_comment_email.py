# Generated by Django 3.0.5 on 2020-04-29 08:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0007_comment'),
    ]

    operations = [
        migrations.AddField(
            model_name='comment',
            name='email',
            field=models.EmailField(default=12, max_length=254),
            preserve_default=False,
        ),
    ]
