# Generated by Django 2.2.28 on 2024-03-12 20:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('gigluvver_app', '0002_auto_20240312_2043'),
    ]

    operations = [
        migrations.AlterField(
            model_name='performer',
            name='Performers',
            field=models.ManyToManyField(blank=True, limit_choices_to={'IsPerformer': True}, to='gigluvver_app.UserProfile'),
        ),
    ]
