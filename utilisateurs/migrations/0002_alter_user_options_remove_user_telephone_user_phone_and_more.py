# Generated by Django 5.2 on 2025-04-18 12:41

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('utilisateurs', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='user',
            options={'ordering': ['last_name', 'first_name'], 'permissions': [('can_promote_agent', ' can promote a client to an agent')], 'verbose_name': 'User', 'verbose_name_plural': 'Users'},
        ),
        migrations.RemoveField(
            model_name='user',
            name='telephone',
        ),
        migrations.AddField(
            model_name='user',
            name='phone',
            field=models.CharField(blank=True, db_column='phone', help_text='main contact number', max_length=20, null=True, validators=[django.core.validators.RegexValidator(message="Format : '+999999999'. Jusqu'à 15 chiffres.", regex='^\\+?1?\\d{9,15}$')], verbose_name='phone'),
        ),
        migrations.AlterField(
            model_name='demandeagent',
            name='statut',
            field=models.CharField(choices=[('Pending', 'Pending'), ('Accepted', 'Accepted'), ('Rejected', 'Rejected')], default='Pending', max_length=20),
        ),
        migrations.AlterField(
            model_name='user',
            name='role',
            field=models.CharField(choices=[('ADMIN', 'Admin'), ('AGENT', 'Agent'), ('CLIENT', 'Client')], default='CLIENT', help_text='Role determining permissions', max_length=20, verbose_name='Role'),
        ),
    ]
