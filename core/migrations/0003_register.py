# Generated by Django 5.0 on 2024-10-10 13:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0002_alter_personinfo_phone'),
    ]

    operations = [
        migrations.CreateModel(
            name='Register',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_date', models.DateField(auto_now_add=True, null=True)),
                ('last_updated_date', models.DateField(auto_now=True, null=True)),
                ('name', models.CharField(max_length=255, verbose_name='Нэр*')),
                ('email', models.EmailField(max_length=255, verbose_name='И-мэйл*')),
                ('phone', models.CharField(max_length=50, verbose_name='Утасны дугаар*')),
            ],
            options={
                'verbose_name': 'login',
                'verbose_name_plural': 'login',
            },
        ),
    ]
