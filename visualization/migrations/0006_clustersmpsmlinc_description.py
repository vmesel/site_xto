# Generated by Django 4.0.2 on 2022-03-25 17:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('visualization', '0005_clustermatrix'),
    ]

    operations = [
        migrations.AddField(
            model_name='clustersmpsmlinc',
            name='description',
            field=models.CharField(blank=True, default='', max_length=2000),
        ),
    ]
