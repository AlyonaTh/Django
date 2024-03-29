# Generated by Django 4.2.6 on 2023-10-12 09:10

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Author',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('firstname', models.CharField(max_length=100)),
                ('lastname', models.CharField(max_length=100)),
                ('email', models.EmailField(max_length=254)),
                ('biography', models.CharField(max_length=300)),
                ('birthdate', models.DateField()),
            ],
        ),
        migrations.CreateModel(
            name='Coin',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('is_eagle', models.CharField(max_length=50)),
                ('create_at', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='Article',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200)),
                ('description', models.CharField(max_length=300)),
                ('create_at', models.DateField(auto_now_add=True)),
                ('category', models.CharField(max_length=100)),
                ('count_views', models.IntegerField(default=0)),
                ('is_published', models.BooleanField(default=False)),
                ('author_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='myapp2.author')),
            ],
        ),
    ]
