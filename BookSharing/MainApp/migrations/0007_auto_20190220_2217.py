# Generated by Django 2.1.3 on 2019-02-20 19:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('MainApp', '0006_auto_20190211_1752'),
    ]

    operations = [
        migrations.AlterField(
            model_name='books',
            name='book',
            field=models.CharField(max_length=120),
        ),
        migrations.AlterField(
            model_name='books',
            name='cont',
            field=models.CharField(max_length=130),
        ),
    ]
