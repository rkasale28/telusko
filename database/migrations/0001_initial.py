# Generated by Django 3.0.4 on 2020-03-17 06:07

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='UserInfo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=15, null=True)),
                ('last_name', models.CharField(max_length=15, null=True)),
                ('email_id', models.EmailField(max_length=254, null=True)),
                ('user_name', models.CharField(max_length=8, null=True)),
                ('pwd', models.CharField(max_length=15, null=True)),
                ('user_type', models.CharField(max_length=10, null=True)),
            ],
        ),
    ]