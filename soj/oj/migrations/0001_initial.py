# Generated by Django 4.2.2 on 2023-06-21 01:47

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Contest',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('contest_name', models.CharField(max_length=16)),
                ('contest_start_time', models.DateTimeField()),
                ('contest_end_time', models.DateTimeField()),
            ],
        ),
        migrations.CreateModel(
            name='Problem',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('problem_name', models.CharField(max_length=16)),
                ('problem_content', models.CharField(max_length=1024)),
                ('problem_memory_limit', models.IntegerField()),
                ('problem_time_limit', models.IntegerField()),
                ('sample_location', models.CharField(max_length=256)),
            ],
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user_name', models.CharField(max_length=16)),
                ('password', models.CharField(max_length=16)),
                ('email', models.CharField(max_length=256)),
            ],
        ),
        migrations.CreateModel(
            name='Grade',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('grade', models.IntegerField()),
                ('memo', models.CharField(max_length=16)),
                ('contest', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='oj.contest')),
                ('problem', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='oj.problem')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='oj.user')),
            ],
        ),
        migrations.AddField(
            model_name='contest',
            name='problem_list',
            field=models.ManyToManyField(to='oj.problem'),
        ),
        migrations.CreateModel(
            name='Code',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('code_location', models.CharField(max_length=256)),
                ('contest', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='oj.contest')),
                ('problem', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='oj.problem')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='oj.user')),
            ],
        ),
    ]
