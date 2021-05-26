# Generated by Django 3.1.1 on 2021-05-26 02:40

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='bookingdetails',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Lid', models.CharField(max_length=50)),
                ('Slid', models.CharField(max_length=50)),
                ('First_name', models.CharField(max_length=50)),
                ('Last_name', models.CharField(max_length=50)),
                ('Email', models.EmailField(max_length=50)),
                ('Mobile', models.CharField(max_length=20)),
                ('Services', models.CharField(max_length=40)),
                ('Date', models.CharField(max_length=50)),
                ('Time', models.TimeField()),
                ('Status', models.CharField(max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='clientlogin',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Username', models.EmailField(max_length=50)),
                ('Password', models.CharField(max_length=250)),
            ],
        ),
        migrations.CreateModel(
            name='contact',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('First_name', models.CharField(max_length=50)),
                ('Last_name', models.CharField(max_length=50)),
                ('Email', models.EmailField(max_length=50)),
                ('Subject', models.CharField(max_length=50)),
                ('Message', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='reviews',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Uid', models.CharField(max_length=50)),
                ('Sid', models.CharField(max_length=50)),
                ('Name', models.CharField(max_length=50)),
                ('Review', models.CharField(max_length=250)),
            ],
        ),
        migrations.CreateModel(
            name='salonlogin',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Username', models.EmailField(max_length=50)),
                ('Password', models.CharField(max_length=250)),
            ],
        ),
        migrations.CreateModel(
            name='salonreg',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('First_name', models.CharField(max_length=50)),
                ('Last_name', models.CharField(max_length=50)),
                ('Email', models.EmailField(max_length=50)),
                ('Password', models.CharField(max_length=250)),
                ('Mobile', models.CharField(max_length=20)),
                ('Address', models.CharField(max_length=250)),
                ('Login_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='user.salonlogin')),
            ],
        ),
        migrations.CreateModel(
            name='salondetails',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Salon_name', models.CharField(max_length=50)),
                ('Opening_hours', models.CharField(max_length=50)),
                ('Services', models.CharField(max_length=300)),
                ('Service_price', models.CharField(max_length=350)),
                ('Image', models.ImageField(upload_to='images')),
                ('Address', models.CharField(max_length=250)),
                ('Login_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='user.salonlogin')),
            ],
        ),
        migrations.CreateModel(
            name='clientreg',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('First_name', models.CharField(max_length=50)),
                ('Last_name', models.CharField(max_length=50)),
                ('Email', models.EmailField(max_length=50)),
                ('Password', models.CharField(max_length=250)),
                ('Mobile', models.CharField(max_length=20)),
                ('Address', models.CharField(max_length=250)),
                ('Login_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='user.clientlogin')),
            ],
        ),
    ]
