# Generated by Django 3.2.4 on 2022-09-07 08:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0006_city_imembership'),
    ]

    operations = [
        migrations.CreateModel(
            name='vgallery',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('vlink', models.TextField()),
                ('vdes', models.TextField()),
                ('vtitle', models.CharField(max_length=50)),
                ('vdate', models.DateField()),
            ],
        ),
        migrations.AlterField(
            model_name='imembership',
            name='mbank',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='imembership',
            name='mpincode',
            field=models.IntegerField(),
        ),
    ]
