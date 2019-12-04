# Generated by Django 2.2.7 on 2019-11-15 22:40

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='zapatilla',
            fields=[
                ('codigo', models.IntegerField(primary_key=True, serialize=False)),
                ('marca', models.CharField(max_length=20)),
                ('modelo', models.CharField(max_length=20)),
                ('precio', models.DecimalField(decimal_places=3, max_digits=6)),
                ('imagen', models.ImageField(null=True, upload_to='items', verbose_name='image')),
            ],
        ),
    ]