# Generated by Django 4.1.6 on 2023-05-26 09:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('paynrentapp', '0007_user_delete_customers'),
    ]

    operations = [
        migrations.CreateModel(
            name='Agencies',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Agencyname', models.CharField(default='', max_length=70)),
                ('mobileno', models.CharField(default='', max_length=15)),
                ('emailid', models.CharField(default='', max_length=150)),
                ('password', models.CharField(default='', max_length=150)),
            ],
        ),
        migrations.DeleteModel(
            name='user',
        ),
    ]
