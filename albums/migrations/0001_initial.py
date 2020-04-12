# Generated by Django 3.0 on 2020-04-12 14:34

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('category_name', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Album',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=50)),
                ('url', models.URLField(default='none')),
                ('image', models.ImageField(default='none', upload_to='images/')),
                ('start_date', models.DateField()),
                ('end_date', models.DateField()),
                ('private', models.BooleanField(default=True)),
                ('categories', models.ManyToManyField(to='albums.Category')),
            ],
        ),
    ]
