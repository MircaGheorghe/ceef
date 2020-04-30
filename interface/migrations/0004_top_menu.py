# Generated by Django 3.0.5 on 2020-04-30 08:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('interface', '0003_auto_20200426_2048'),
    ]

    operations = [
        migrations.CreateModel(
            name='Top_menu',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('item_title', models.CharField(max_length=100, verbose_name='Itemi de nivelul 3')),
                ('numarul_de_ordine', models.IntegerField(default=1, verbose_name='Numărul de ordine în meniu')),
                ('pub_date', models.DateTimeField(auto_now_add=True, verbose_name='Data publicarii')),
            ],
            options={
                'verbose_name': 'Item din top meniu',
                'verbose_name_plural': 'Itemi din top meniu',
            },
        ),
    ]
