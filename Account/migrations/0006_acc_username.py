# Generated by Django 3.1.4 on 2020-12-11 10:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Account', '0005_acc_is_staff'),
    ]

    operations = [
        migrations.AddField(
            model_name='acc',
            name='username',
            field=models.CharField(default=True, max_length=60, verbose_name='email'),
        ),
    ]
