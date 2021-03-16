# Generated by Django 3.0 on 2020-04-21 11:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pages', '0002_auto_20200421_0222'),
    ]

    operations = [
        migrations.AddField(
            model_name='housing',
            name='publish_date',
            field=models.DateTimeField(auto_now=True),
        ),
        migrations.AlterField(
            model_name='housing',
            name='Inside_Photo',
            field=models.ImageField(default=None, upload_to='images/home'),
        ),
        migrations.AlterField(
            model_name='housing',
            name='Main_Photo',
            field=models.ImageField(default=None, upload_to='images/home'),
        ),
        migrations.AlterField(
            model_name='realtor',
            name='image',
            field=models.ImageField(default=None, upload_to='images/realtor'),
        ),
    ]