# Generated by Django 5.0.7 on 2024-07-22 20:17

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
            name='Location',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('county', models.CharField(max_length=100)),
                ('city', models.CharField(max_length=100)),
                ('state', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Hotspot',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.URLField(max_length=500, null=True)),
                ('category', models.CharField(choices=[('daytime', 'Daytime'), ('nightlife', 'Nightlife')], max_length=100)),
                ('name', models.CharField(max_length=255)),
                ('address', models.CharField(max_length=255)),
                ('city', models.CharField(max_length=100)),
                ('state', models.CharField(max_length=100)),
                ('zip_code', models.CharField(max_length=20)),
                ('phone_number', models.CharField(blank=True, max_length=20)),
                ('website', models.URLField(blank=True)),
                ('opening_time', models.TimeField(blank=True, null=True)),
                ('closing_time', models.TimeField(blank=True, null=True)),
                ('price_range', models.CharField(blank=True, choices=[('$-$$', 'Low to Medium'), ('$$-$$$', 'Medium to High'), ('$$$-$$$$', 'High End')], max_length=10)),
                ('description', models.TextField(blank=True, default='no description')),
                ('location', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='hotspots', to='XploreATL.location')),
            ],
        ),
        migrations.CreateModel(
            name='Eatery',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.URLField(max_length=500, null=True)),
                ('category', models.CharField(choices=[('restaurant', 'Restaurant'), ('cafe', 'Cafe'), ('bakery', 'Bakery')], max_length=100)),
                ('name', models.CharField(max_length=255)),
                ('address', models.CharField(max_length=255)),
                ('city', models.CharField(max_length=100)),
                ('state', models.CharField(max_length=100)),
                ('zip_code', models.CharField(max_length=20)),
                ('cuisine', models.CharField(blank=True, max_length=255)),
                ('phone_number', models.CharField(blank=True, max_length=20)),
                ('website', models.URLField(blank=True)),
                ('opening_time', models.TimeField(blank=True, null=True)),
                ('closing_time', models.TimeField(blank=True, null=True)),
                ('price_range', models.CharField(blank=True, choices=[('$-$$', 'Low to Medium'), ('$$-$$$', 'Medium to High'), ('$$$-$$$$', 'High End')], max_length=10)),
                ('description', models.TextField(blank=True, default='no description')),
                ('location', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='eateries', to='XploreATL.location')),
            ],
        ),
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('bookmarked_eateries', models.ManyToManyField(blank=True, related_name='bookmarked_by', to='XploreATL.eatery')),
                ('bookmarked_hotspots', models.ManyToManyField(blank=True, related_name='bookmarked_by', to='XploreATL.hotspot')),
                ('favorite_eateries', models.ManyToManyField(blank=True, related_name='favorited_by', to='XploreATL.eatery')),
                ('favorite_hotspots', models.ManyToManyField(blank=True, related_name='favorited_by', to='XploreATL.hotspot')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
