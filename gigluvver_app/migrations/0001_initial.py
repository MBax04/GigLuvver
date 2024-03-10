# Generated by Django 2.2.28 on 2024-03-10 01:34

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Performer',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('UserName', models.CharField(max_length=128, unique=True)),
                ('StageName', models.CharField(max_length=128)),
                ('Genre', models.CharField(max_length=128)),
                ('ProfilePicture', models.ImageField(blank=True, upload_to='profile_images')),
            ],
        ),
        migrations.CreateModel(
            name='Venue',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('VenueName', models.CharField(max_length=128, unique=True)),
                ('Location', models.CharField(max_length=128)),
            ],
        ),
        migrations.CreateModel(
            name='Gig',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('GigID', models.CharField(max_length=128, unique=True)),
                ('Date', models.DateField()),
                ('Time', models.TimeField()),
                ('ProfilePicture', models.ImageField(blank=True, upload_to='gig_images')),
                ('PerformerStageNames', models.ManyToManyField(to='gigluvver_app.Performer')),
                ('Venue', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='gigluvver_app.Venue')),
            ],
        ),
        migrations.CreateModel(
            name='Attendee',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('UserName', models.CharField(max_length=128, unique=True)),
                ('Gigs', models.ManyToManyField(to='gigluvver_app.Gig')),
            ],
        ),
    ]
