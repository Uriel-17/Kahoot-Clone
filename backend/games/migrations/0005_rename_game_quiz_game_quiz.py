# Generated by Django 4.0.3 on 2022-03-08 06:54

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('games', '0004_player_answers_delete_playeranswerlist'),
    ]

    operations = [
        migrations.RenameField(
            model_name='game',
            old_name='game_quiz',
            new_name='quiz',
        ),
    ]