# Generated by Django 3.0.6 on 2020-06-18 18:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('createBlog', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='contact',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('firstname', models.TextField(max_length=30, null=True)),
                ('lastname', models.TextField(max_length=30, null=True)),
                ('email', models.TextField(max_length=20, null=True)),
                ('address', models.CharField(max_length=50, null=True)),
                ('description', models.CharField(max_length=256, null=True)),
            ],
        ),
    ]
