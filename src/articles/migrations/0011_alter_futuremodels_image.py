# Generated by Django 3.2.6 on 2021-08-12 11:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('articles', '0010_alter_mainsitemodels_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='futuremodels',
            name='image',
            field=models.ImageField(blank=True, upload_to='media/images/'),
        ),
    ]
