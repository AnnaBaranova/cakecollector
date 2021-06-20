# Generated by Django 3.1.7 on 2021-06-20 20:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0002_combo'),
    ]

    operations = [
        migrations.CreateModel(
            name='Topping',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20)),
                ('portion', models.IntegerField()),
            ],
        ),
        migrations.AlterModelOptions(
            name='combo',
            options={'ordering': ['date']},
        ),
    ]
