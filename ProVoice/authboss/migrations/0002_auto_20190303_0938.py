# Generated by Django 2.1.7 on 2019-03-03 03:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('authboss', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='profile',
            options={'verbose_name': 'Профиль', 'verbose_name_plural': 'Профили'},
        ),
        migrations.AddField(
            model_name='profile',
            name='student',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='profile',
            name='teacher',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='profile',
            name='show_name',
            field=models.BooleanField(default=False, verbose_name='Показать имя на сайте'),
        ),
    ]