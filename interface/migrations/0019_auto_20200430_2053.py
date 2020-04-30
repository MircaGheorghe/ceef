# Generated by Django 3.0.5 on 2020-04-30 17:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('interface', '0018_comments'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='comments',
            options={'verbose_name': 'Comentariu', 'verbose_name_plural': 'Comentarii'},
        ),
        migrations.AddField(
            model_name='comments',
            name='name',
            field=models.TextField(default=1, verbose_name='Numele'),
            preserve_default=False,
        ),
    ]