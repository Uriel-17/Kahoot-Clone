# Generated by Django 4.0.3 on 2022-03-12 00:24

from django.conf import settings
import django.core.validators
from django.db import migrations, models
import django.db.models.deletion
import django_fsm
import re


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('quizzes', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Game',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('state', django_fsm.FSMField(default='active', max_length=50, protected=True)),
                ('slug', models.CharField(max_length=5, unique=True)),
                ('creator', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='games', to=settings.AUTH_USER_MODEL)),
                ('current_question', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='game', to='quizzes.question')),
                ('quiz', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='quizzes.quiz')),
            ],
        ),
        migrations.CreateModel(
            name='Player',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('email', models.EmailField(max_length=254)),
                ('slug', models.CharField(max_length=5, unique=True)),
                ('answers', models.CharField(max_length=100, validators=[django.core.validators.RegexValidator(re.compile('^\\d+(?:,\\d+)*\\Z'), code='invalid', message='Enter only digits separated by commas.')])),
                ('game', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='players', to='games.game')),
            ],
        ),
    ]
