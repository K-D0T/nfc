# Generated by Django 3.1.7 on 2021-03-09 16:30

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='SignUpModel',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('tag', models.IntegerField(null=True)),
                ('email', models.CharField(max_length=225)),
                ('password', models.CharField(max_length=225)),
            ],
        ),
    ]
