# Generated by Django 4.2.7 on 2024-02-14 05:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0007_alter_comment_user_alter_post_author'),
    ]

    operations = [
        migrations.CreateModel(
            name='feedbacks',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('filename', models.CharField(max_length=50)),
                ('time', models.DateTimeField(auto_now_add=True)),
                ('filelocation', models.FileField(upload_to='feedbacks/')),
            ],
        ),
        migrations.AlterField(
            model_name='normuser',
            name='profilePic',
            field=models.ImageField(null=True, upload_to='media/profilePics/'),
        ),
    ]
