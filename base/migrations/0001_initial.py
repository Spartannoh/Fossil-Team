# Generated by Django 5.0.4 on 2024-04-14 12:55

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Task',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('título', models.CharField(blank=True, max_length=200, null=True)),
                ('descrição', models.TextField(blank=True, null=True)),
                ('completa', models.BooleanField(default=False)),
                ('criar', models.DateTimeField(auto_now_add=True)),
                ('usuário', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'ordering': ['completa'],
            },
        ),
    ]