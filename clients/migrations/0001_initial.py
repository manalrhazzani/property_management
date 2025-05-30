# Generated by Django 5.2 on 2025-04-14 23:50

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('biens', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Interaction',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('type_interaction', models.CharField(choices=[('Appel', 'Appel'), ('Visite', 'Visite'), ('Rendez-vous', 'Rendez-vous'), ('Note', 'Note')], max_length=20)),
                ('commentaire', models.TextField()),
                ('date', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='Client',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nom', models.CharField(max_length=100)),
                ('prenom', models.CharField(max_length=100)),
                ('email', models.EmailField(max_length=254, unique=True)),
                ('telephone', models.CharField(max_length=15)),
                ('type_client', models.CharField(choices=[('Acheteur', 'Acheteur'), ('Locataire', 'Locataire')], default='Acheteur', max_length=10)),
                ('bien', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='clients_interesses', to='biens.bien')),
            ],
        ),
    ]
