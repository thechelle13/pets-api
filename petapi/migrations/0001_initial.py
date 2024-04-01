# Generated by Django 4.2.7 on 2024-03-28 15:15

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
            name='Pet',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=155)),
                ('image_url', models.URLField()),
            ],
        ),
        migrations.CreateModel(
            name='PetUser',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('bio', models.CharField(max_length=200)),
                ('city', models.CharField(max_length=155)),
                ('created_on', models.DateTimeField(auto_now_add=True)),
                ('active', models.BooleanField()),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='pet_user', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Type',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('label', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('description', models.CharField(max_length=200)),
                ('sitStartDate', models.DateField()),
                ('sitEndDate', models.DateField()),
                ('publication_date', models.DateField(auto_now_add=True)),
                ('approved', models.BooleanField()),
                ('pet', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='petapi.pet')),
                ('pet_user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='posts', to='petapi.petuser')),
            ],
        ),
        migrations.AddField(
            model_name='pet',
            name='type',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='petapi.type'),
        ),
        migrations.AddField(
            model_name='pet',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]
