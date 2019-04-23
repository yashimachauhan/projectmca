# Generated by Django 2.0.6 on 2019-04-16 07:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('userapp', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='SignUpUser',
            fields=[
                ('first_name', models.CharField(default='', max_length=225)),
                ('last_name', models.CharField(default='', max_length=225)),
                ('email', models.CharField(default='', max_length=225, primary_key=True, serialize=False)),
                ('confirm_password', models.CharField(default='', max_length=20)),
                ('SignUp_time', models.CharField(default='', max_length=255)),
                ('SignUp_date', models.CharField(default='', max_length=255)),
            ],
        ),
        migrations.AddField(
            model_name='userinfo',
            name='otp',
            field=models.CharField(default='', max_length=225, null='True'),
        ),
        migrations.AddField(
            model_name='userinfo',
            name='otptime',
            field=models.CharField(default='', max_length=225, null='True'),
        ),
    ]
