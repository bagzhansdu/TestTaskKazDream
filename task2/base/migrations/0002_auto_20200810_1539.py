# Generated by Django 3.0.8 on 2020-08-10 09:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='lesson',
            options={'verbose_name': 'Урок', 'verbose_name_plural': 'Уроки'},
        ),
        migrations.RemoveField(
            model_name='student',
            name='lesson',
        ),
        migrations.AddField(
            model_name='student',
            name='lesson',
            field=models.ManyToManyField(to='base.Lesson'),
        ),
    ]
