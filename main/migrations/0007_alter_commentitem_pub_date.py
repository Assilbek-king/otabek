# Generated by Django 3.2.12 on 2022-07-30 20:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0006_alter_commentitem_pub_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='commentitem',
            name='pub_date',
            field=models.DateField(),
        ),
    ]