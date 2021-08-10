# Generated by Django 3.2.4 on 2021-07-31 11:18

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Callback',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=120, verbose_name='Имя')),
                ('phone', models.CharField(max_length=100, verbose_name='Tелефон')),
                ('timestamp', models.DateTimeField(auto_now_add=True, verbose_name='Дата заявки')),
            ],
            options={
                'verbose_name': 'Заявка на обратный звонок',
                'verbose_name_plural': 'Заявки на обратный звонок',
                'ordering': ['-id', '-timestamp'],
            },
        ),
    ]