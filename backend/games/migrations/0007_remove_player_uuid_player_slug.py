# Generated by Django 4.0.3 on 2022-03-08 21:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('games', '0006_alter_game_state'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='player',
            name='UUID',
        ),
        migrations.AddField(
            model_name='player',
            name='slug',
            field=models.CharField(default=None, max_length=5, unique=True),
            preserve_default=False,
        ),
    ]