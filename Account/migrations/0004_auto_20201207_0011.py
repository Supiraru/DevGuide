# Generated by Django 3.1.4 on 2020-12-06 17:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Account', '0003_biodata'),
    ]

    operations = [
        migrations.AlterField(
            model_name='biodata',
            name='username',
            field=models.CharField(blank=True, max_length=50, null=True, unique=True, verbose_name='Username'),
        ),
    ]
