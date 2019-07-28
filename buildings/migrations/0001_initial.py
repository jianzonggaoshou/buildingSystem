# Generated by Django 2.0.6 on 2019-07-20 01:50

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Buildings',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('building_id', models.IntegerField(unique=True, verbose_name='楼房id')),
                ('name', models.CharField(blank=True, max_length=128, null=True, verbose_name='房屋名')),
                ('households', models.IntegerField(blank=True, null=True, verbose_name='户数')),
                ('location', models.CharField(blank=True, max_length=128, null=True, verbose_name='位置')),
                ('image', models.ImageField(upload_to='')),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
            ],
            options={
                'ordering': ('id',),
            },
        ),
    ]
