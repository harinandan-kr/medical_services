# Generated by Django 3.2.6 on 2021-08-07 08:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('display', '0006_auto_20210518_2040'),
    ]

    operations = [
        migrations.CreateModel(
            name='medical_storesservice',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('medical_storesservice_name', models.CharField(default='', max_length=80)),
                ('medical_storesservice_state', models.CharField(default='', max_length=30)),
                ('medical_storesservice_city', models.CharField(default='', max_length=30)),
                ('medical_storesservice_area', models.CharField(default='', max_length=120)),
                ('medical_storesservice_address', models.CharField(default='', max_length=120)),
                ('medical_storesservice_pincode', models.IntegerField(default='')),
                ('medical_storesservice_price', models.IntegerField(default='0')),
                ('medical_storesservice_contactnumber', models.IntegerField(default='+91')),
                ('medical_storesservice_mealtype', models.CharField(default='veg', max_length=120)),
                ('medical_storesservice_mealsperday', models.IntegerField(default=3)),
                ('medical_storesservice_description', models.TextField(default='', max_length=500)),
                ('medical_storesservice_images1', models.ImageField(default='', upload_to='display/img/medical_stores_service_images')),
                ('medical_storesservice_image2', models.ImageField(default='', upload_to='display/img/medical_stores_service_images')),
            ],
        ),
        migrations.DeleteModel(
            name='tiffinservice',
        ),
    ]
