# Generated by Django 3.1.4 on 2021-01-05 10:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('newblog', '0003_post_post_date'),
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=25)),
            ],
        ),
        migrations.AddField(
            model_name='post',
            name='category',
            field=models.CharField(default='Random', max_length=30),
        ),
        migrations.AlterField(
            model_name='post',
            name='title_tag',
            field=models.CharField(default='Hot News', max_length=25),
        ),
    ]
