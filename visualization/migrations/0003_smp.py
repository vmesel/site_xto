# Generated by Django 2.0.1 on 2018-05-23 20:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('visualization', '0002_genelocation_link'),
    ]

    operations = [
        migrations.CreateModel(
            name='Smp',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('smp', models.CharField(default='', max_length=256)),
            ],
        ),
    ]