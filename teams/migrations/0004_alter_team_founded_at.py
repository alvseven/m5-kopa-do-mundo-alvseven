# Generated by Django 4.1.3 on 2022-11-25 16:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('teams', '0003_alter_team_founded_at'),
    ]

    operations = [
        migrations.AlterField(
            model_name='team',
            name='founded_at',
            field=models.DateField(null=True),
        ),
    ]
