# Generated by Django 4.1 on 2022-09-07 12:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hello', '0004_logmessage_subject_alter_logmessage_message_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='logmessage',
            name='email',
            field=models.CharField(max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='logmessage',
            name='message',
            field=models.CharField(max_length=400, null=True),
        ),
        migrations.AlterField(
            model_name='logmessage',
            name='name',
            field=models.CharField(max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='logmessage',
            name='severity',
            field=models.IntegerField(choices=[(1, '1'), (2, '2'), (3, '3'), (4, '4'), (5, '5')], default=5),
        ),
        migrations.AlterField(
            model_name='logmessage',
            name='subject',
            field=models.CharField(max_length=100, null=True),
        ),
    ]