# Generated by Django 5.2 on 2025-04-18 13:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('rendezvous', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='rendezvous',
            old_name='commentaire',
            new_name='comment',
        ),
        migrations.RenameField(
            model_name='rendezvous',
            old_name='bien',
            new_name='property',
        ),
        migrations.RenameField(
            model_name='rendezvous',
            old_name='heure',
            new_name='time',
        ),
        migrations.RemoveField(
            model_name='rendezvous',
            name='statut',
        ),
        migrations.AddField(
            model_name='rendezvous',
            name='status',
            field=models.CharField(choices=[('Scheduled', 'Scheduled'), ('Completed', 'Completed'), ('Canceled', 'Canceled')], default='Scheduled', max_length=20),
        ),
    ]
