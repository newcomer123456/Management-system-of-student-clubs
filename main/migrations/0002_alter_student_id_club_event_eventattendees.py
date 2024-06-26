# Generated by Django 5.0.6 on 2024-06-26 12:02

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='student',
            name='id',
            field=models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
        migrations.CreateModel(
            name='Club',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('description', models.CharField(max_length=400)),
                ('members', models.ManyToManyField(related_name='member_clubs', to='main.student')),
                ('president', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='presided_clubs', to='main.student')),
            ],
        ),
        migrations.CreateModel(
            name='Event',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('date', models.DateField()),
                ('venue', models.CharField(max_length=100)),
                ('club', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='events', to='main.club')),
                ('participants', models.ManyToManyField(related_name='attended_events', to='main.student')),
            ],
        ),
        migrations.CreateModel(
            name='EventAttendees',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('event', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='attendees', to='main.event')),
                ('student', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='event_attendances', to='main.student')),
            ],
        ),
    ]