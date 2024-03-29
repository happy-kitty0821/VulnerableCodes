# Generated by Django 4.2.7 on 2024-01-31 07:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('loginapp', '0002_feedbacks'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='contact',
            field=models.CharField(default='0000000000', max_length=20),
        ),
        migrations.AddField(
            model_name='user',
            name='email',
            field=models.EmailField(default='user@email.com.uk', max_length=100),
        ),
        migrations.AlterField(
            model_name='feedbacks',
            name='contact',
            field=models.CharField(default='0000000000', max_length=15),
        ),
    ]
