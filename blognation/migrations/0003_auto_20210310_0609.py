# Generated by Django 3.1.4 on 2021-03-10 06:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blognation', '0002_auto_20210106_1506'),
    ]

    operations = [
        migrations.CreateModel(
            name='Data',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('email', models.CharField(max_length=100)),
                ('cloth', models.TextField()),
                ('dimension', models.DecimalField(decimal_places=3, max_digits=100)),
            ],
        ),
        migrations.DeleteModel(
            name='Blog',
        ),
    ]
