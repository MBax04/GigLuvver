# Generated by Django 2.1.5 on 2024-03-16 18:52

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Attendees',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
        ),
        migrations.CreateModel(
            name='Gig',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('GigID', models.CharField(max_length=128, unique=True)),
                ('GigName', models.CharField(default='Default Name', max_length=128, unique=True)),
                ('Date', models.DateField()),
                ('Time', models.TimeField()),
                ('GigPicture', models.ImageField(blank=True, upload_to='./media/gig_images')),
            ],
        ),
        migrations.CreateModel(
            name='Performer',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('PerformerGig', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='gigluvver_app.Gig')),
            ],
        ),
        migrations.CreateModel(
            name='UserProfile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('IsPerformer', models.BooleanField(default=False)),
                ('StageName', models.CharField(blank=True, max_length=128, null=True, unique=True)),
                ('Genre', models.CharField(blank=True, max_length=128)),
                ('ProfilePicture', models.ImageField(blank=True, upload_to='./media/profile_images')),
                ('UserField', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
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
        migrations.AddField(
            model_name='performer',
            name='Performers',
            field=models.ManyToManyField(blank=True, limit_choices_to={'IsPerformer': True}, to='gigluvver_app.UserProfile'),
        ),
        migrations.AddField(
            model_name='gig',
            name='Venue',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='gigluvver_app.Venue'),
        ),
        migrations.AddField(
            model_name='attendees',
            name='Attendee',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='gigluvver_app.UserProfile'),
        ),
        migrations.AddField(
            model_name='attendees',
            name='Gigs',
            field=models.ManyToManyField(blank=True, to='gigluvver_app.Gig'),
        ),
    ]
