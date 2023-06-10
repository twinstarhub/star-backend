# Generated by Django 2.2.26 on 2022-09-20 13:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0004_businessyearinterval_currencylist_introduceyourself_numberofstaff_petsittingsoftware'),
    ]

    operations = [
        migrations.CreateModel(
            name='Vet',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=255, null=True, verbose_name='Name')),
                ('email', models.EmailField(max_length=254, verbose_name='Email')),
                ('work_phone', models.CharField(blank=True, max_length=255, null=True, verbose_name='Phone Number')),
                ('address1', models.CharField(blank=True, max_length=255, null=True, verbose_name='Address1')),
                ('address2', models.CharField(blank=True, max_length=255, null=True, verbose_name='Address2')),
                ('city', models.CharField(blank=True, max_length=255, null=True, verbose_name='City')),
                ('zip', models.CharField(blank=True, max_length=255, null=True, verbose_name='Zip')),
                ('state', models.CharField(blank=True, max_length=255, null=True, verbose_name='State')),
                ('notes', models.TextField()),
            ],
        ),
        # migrations.AlterField(
        #     model_name='introduceyourself',
        #     name='company_website',
        #     field=models.URLField(unique=True),
        # ),
    ]