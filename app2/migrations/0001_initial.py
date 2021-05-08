# Generated by Django 3.2.1 on 2021-05-07 12:35

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Post2',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('post2_title', models.CharField(max_length=200)),
                ('post2_writer', models.CharField(max_length=100)),
                ('post2_date', models.DateTimeField()),
                ('post2_body', models.TextField()),
                ('image', models.ImageField(blank=True, null=True, upload_to='post/')),
            ],
        ),
    ]