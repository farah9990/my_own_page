# Generated by Django 5.0.2 on 2024-03-23 11:43

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='History',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Search', models.CharField(max_length=255)),
                ('Date', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]
