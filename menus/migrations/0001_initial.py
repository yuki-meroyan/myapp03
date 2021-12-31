# Generated by Django 3.2.10 on 2021-12-31 07:02

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Stock',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=50)),
                ('amount', models.IntegerField()),
                ('unit', models.CharField(max_length=10)),
                ('limit_date', models.DateTimeField()),
                ('create_user', models.CharField(max_length=150)),
                ('update_user', models.CharField(max_length=150)),
                ('create_date', models.DateTimeField()),
                ('update_date', models.DateTimeField()),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Menu',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('menu_number', models.IntegerField()),
                ('menu_name', models.CharField(max_length=50)),
                ('create_user', models.CharField(max_length=150)),
                ('update_user', models.CharField(max_length=150)),
                ('create_date', models.DateTimeField()),
                ('update_date', models.DateTimeField()),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Material',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=50)),
                ('amount', models.IntegerField()),
                ('unit', models.CharField(max_length=10)),
                ('create_user', models.CharField(max_length=150)),
                ('update_user', models.CharField(max_length=150)),
                ('create_date', models.DateTimeField()),
                ('update_date', models.DateTimeField()),
                ('menu', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='menus.menu')),
                ('stock', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='menus.stock')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
