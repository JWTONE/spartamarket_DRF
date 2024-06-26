# Generated by Django 4.2 on 2024-04-30 04:32

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Products',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(default='', max_length=30)),
                ('content', models.TextField(blank=True)),
                ('images', models.ImageField(upload_to='./products/')),
                ('price', models.IntegerField()),
            ],
        ),
    ]
