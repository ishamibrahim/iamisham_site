# Generated by Django 4.2.2 on 2024-01-24 10:56

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('iamisham_app', '0001_initial'),
    ]

    operations = [
        migrations.AlterUniqueTogether(
            name='choice',
            unique_together=set(),
        ),
        migrations.AlterField(
            model_name='choice',
            name='choice_text',
            field=models.CharField(max_length=200, unique=True),
        ),
        migrations.RemoveField(
            model_name='choice',
            name='is_correct',
        ),
        migrations.RemoveField(
            model_name='choice',
            name='question',
        ),
        migrations.CreateModel(
            name='CorrectChoice',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_date', models.DateTimeField(auto_now_add=True)),
                ('updated_date', models.DateTimeField(auto_now=True)),
                ('choice', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='iamisham_app.choice')),
                ('question', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='iamisham_app.question')),
            ],
            options={
                'unique_together': {('question', 'choice')},
            },
        ),
        migrations.AddField(
            model_name='choice',
            name='question',
            field=models.ManyToManyField(to='iamisham_app.question'),
        ),
    ]
