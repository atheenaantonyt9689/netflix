# Generated by Django 3.1.5 on 2021-06-08 14:13

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Netflix',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Title', models.CharField(max_length=100)),
                ('Genre', models.CharField(max_length=100)),
                ('Premiere', models.CharField(max_length=100)),
                ('Runtime', models.CharField(max_length=100)),
                ('IMDB_Score', models.CharField(max_length=100)),
                ('Language', models.CharField(max_length=100)),
            ],
        ),
    ]
