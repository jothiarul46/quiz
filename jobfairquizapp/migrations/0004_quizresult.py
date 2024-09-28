# Generated by Django 5.0 on 2024-09-28 07:34

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('jobfairquizapp', '0003_rename_question_quizquestion_alter_quiz_options_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='QuizResult',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user_answer', models.CharField(max_length=255)),
                ('question', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='jobfairquizapp.quizquestion')),
                ('quiz', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='jobfairquizapp.quiz')),
            ],
            options={
                'verbose_name': 'Quiz Result',
                'verbose_name_plural': 'Quiz Results',
            },
        ),
    ]
