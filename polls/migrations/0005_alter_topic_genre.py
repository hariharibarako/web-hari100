# Generated by Django 4.0.2 on 2022-03-15 13:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0004_alter_topic_genre'),
    ]

    operations = [
        migrations.AlterField(
            model_name='topic',
            name='genre',
            field=models.CharField(choices=[('IT', 'IT'), ('Accountant', 'Accountant'), ('Everyday', 'Everyday'), ('Eye', 'Eye'), ('ハリネズミ', 'ハリネズミ'), ('Python(Django)', 'Python(Django)'), ('Swift', 'Swift')], default='Everyday', max_length=100),
        ),
    ]
