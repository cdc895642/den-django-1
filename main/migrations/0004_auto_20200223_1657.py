# Generated by Django 3.0.2 on 2020-02-23 14:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0003_post_download'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='category',
            field=models.CharField(blank=True, choices=[('Multimedia', 'multimedia'), ('Games', 'games')], max_length=20, null=True),
        ),
    ]
